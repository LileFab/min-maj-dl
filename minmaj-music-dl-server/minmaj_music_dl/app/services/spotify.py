import json
import logging
import os
import re
import threading
from subprocess import run
from app.services import spotify_auth as sp_auth_sv
from app.schemas import SpotifyPlaylist
from app.clients import spotify as sp_client
from app.constants import DESTINATION_FOLDER, SPOTIFY_STATE_DIR

logger = logging.getLogger(__name__)

SPOTIFY_URL_RE = re.compile(
    r"^https://open\.spotify\.com/(?:intl-[a-z]{2}(?:-[a-z]{2})?/)?(playlist|album|track|artist)/([A-Za-z0-9]+)"
)


def get_playlists() -> list[SpotifyPlaylist]:
    access_token = sp_auth_sv.get_or_refresh_sp_token().access_token

    json_data = sp_client.get_playlists(access_token=access_token)

    return [SpotifyPlaylist(**pl) for pl in json_data]


def normalize_spotify_url(url: str) -> str | None:
    """Retourne l'URL Spotify nettoyée (sans ?si=...), ou None si invalide"""
    match = SPOTIFY_URL_RE.match(url.strip())
    if not match:
        return None
    kind, spotify_id = match.groups()
    return f"https://open.spotify.com/{kind}/{spotify_id}"


# Caractères interdits dans un nom de dossier (Samba / Windows / macOS) remplacés
# par leurs équivalents visuels, comme le fait déjà yt-dlp (ex. "02⧸11")
_FOLDER_CHARS = str.maketrans({
    "/": "⧸", "\\": "＼", ":": "：", "*": "＊", "?": "？",
    '"': "＂", "<": "＜", ">": "＞", "|": "｜",
})


def _folder_name(name: str) -> str:
    cleaned = "".join(c for c in name if c.isprintable()).translate(_FOLDER_CHARS)
    return cleaned.strip().strip(".") or "Sans titre"


def _fetch_list_name(kind: str, spotify_id: str) -> str | None:
    """Nom actuel de la playlist / album / artiste (sans token, via SpotipyFree)"""
    try:
        from SpotipyFree import Spotify

        sp = Spotify()
        getter = {"playlist": sp.playlist, "album": sp.album, "artist": sp.artist}[kind]
        return (getter(spotify_id) or {}).get("name")
    except Exception:
        logger.exception("Impossible de récupérer le nom de %s/%s", kind, spotify_id)
        return None


def _resolve_folder(kind: str, spotify_id: str) -> str | None:
    """Dossier de destination ; renomme l'ancien dossier si la liste a changé de nom"""
    name = _fetch_list_name(kind, spotify_id)
    if not name:
        return None
    folder = _folder_name(name)

    state_file = os.path.join(SPOTIFY_STATE_DIR, f"{kind}-{spotify_id}.json")
    try:
        with open(state_file) as f:
            previous = json.load(f).get("folder")
    except (OSError, ValueError):
        previous = None

    if previous and previous != folder:
        old_path = os.path.join(DESTINATION_FOLDER, previous)
        new_path = os.path.join(DESTINATION_FOLDER, folder)
        if os.path.isdir(old_path) and not os.path.exists(new_path):
            os.rename(old_path, new_path)
            logger.info("Dossier renommé : %s -> %s", previous, folder)

    with open(state_file, "w") as f:
        json.dump({"folder": folder, "name": name}, f, ensure_ascii=False)
    return folder


def _run_spotdl(url: str) -> None:
    try:
        kind, spotify_id = SPOTIFY_URL_RE.match(url).groups()
        os.makedirs(SPOTIFY_STATE_DIR, exist_ok=True)

        if kind == "track":
            output = f"{DESTINATION_FOLDER}/{{artists}} - {{title}}.{{output-ext}}"
        else:
            folder = _resolve_folder(kind, spotify_id)
            # Si le nom n'a pas pu être récupéré, on laisse spotdl nommer le dossier
            folder_tpl = folder.replace("{", "{{").replace("}", "}}") if folder else "{list-name}"
            output = f"{DESTINATION_FOLDER}/{folder_tpl}/{{artists}} - {{title}}.{{output-ext}}"

        result = run(
            [
                "spotdl", "download", url,
                "--format", "mp3",
                "--bitrate", "320k",
                "--threads", "4",
                # Une archive par playlist : un titre présent dans plusieurs
                # playlists est bien téléchargé dans chacune
                "--archive", os.path.join(SPOTIFY_STATE_DIR, f"{kind}-{spotify_id}.archive.txt"),
                "--output", output,
            ]
        )
        if result.returncode == 0:
            logger.info("Téléchargement Spotify terminé: %s", url)
        else:
            logger.error("spotdl a échoué (code %s) pour %s", result.returncode, url)
    except Exception:
        logger.exception("Erreur pendant le téléchargement Spotify de %s", url)


def download_song_or_playlist(url: str) -> dict:
    """Lance en arrière-plan le téléchargement d'un titre / album / playlist Spotify"""
    clean_url = normalize_spotify_url(url)
    if clean_url is None:
        return {
            "success": False,
            "message": "URL Spotify invalide",
            "destination": DESTINATION_FOLDER,
        }

    try:
        os.makedirs(DESTINATION_FOLDER, exist_ok=True)

        # Pas de --auth-token : notre token "client_credentials" n'est pas un
        # token utilisateur, et Spotify le refuse (401) pour lire les playlists.
        # spotdl se débrouille seul pour récupérer les métadonnées.
        threading.Thread(target=_run_spotdl, args=(clean_url,), daemon=True).start()

        return {
            "success": True,
            "message": "Téléchargement lancé",
            "destination": DESTINATION_FOLDER,
        }
    except Exception as e:
        return {
            "success": False,
            "message": f"Erreur: {str(e)}",
            "destination": DESTINATION_FOLDER,
        }
