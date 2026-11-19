import logging
import os
import re
import threading
from subprocess import run
from urllib.parse import urlparse
from app.services import credentials as credentials_sv
from app.services import soundcloud_auth as sc_auth_sv
from app.schemas import SoundcloudPlaylist, SoundcloudTrack
from app.clients import soundcloud as sc_client
from app.constants import (
    DESTINATION_FOLDER,
    SOUNDCLOUD_BASE_URL,
    SOUNDCLOUD_LIKES_FOLDER,
    SOUNDCLOUD_STATE_DIR,
)

logger = logging.getLogger(__name__)


def get_playlists() -> list[SoundcloudPlaylist]:
    user_id = credentials_sv.get().soundcloud_user_id
    access_token = sc_auth_sv.get_or_refresh_sc_token().access_token

    json_data = sc_client.get_playlists(user_id=user_id, access_token=access_token)

    return [SoundcloudPlaylist(**pl) for pl in json_data]


def get_username() -> str:
    user_id = credentials_sv.get().soundcloud_user_id
    access_token = sc_auth_sv.get_or_refresh_sc_token().access_token

    return sc_client.get_username(user_id=user_id, access_token=access_token)


def _archive_for(url: str, suffix: str = "") -> str:
    """Une archive par URL : un titre présent dans plusieurs playlists est
    bien téléchargé dans chacune"""
    path = urlparse(url).path.strip("/") or "root"
    slug = re.sub(r"[^A-Za-z0-9_-]+", "_", path) + suffix
    return os.path.join(SOUNDCLOUD_STATE_DIR, f"{slug}.archive.txt")


def _run_scdl(url: str, path: str, archive: str, extra_args: list[str]) -> None:
    try:
        result = run(
            [
                "scdl", "-l", url,
                *extra_args,
                "--path", path,
                "--original-name", "--addtofile",
                "--download-archive", archive,
            ]
        )
        if result.returncode == 0:
            logger.info("Téléchargement SoundCloud terminé: %s", url)
        else:
            logger.error("scdl a échoué (code %s) pour %s", result.returncode, url)
    except Exception:
        logger.exception("Erreur pendant le téléchargement SoundCloud de %s", url)


def _start_download(url: str, path: str = DESTINATION_FOLDER, extra_args: list[str] | None = None, archive_suffix: str = "") -> dict:
    """Lance scdl en arrière-plan (évite le timeout gunicorn) et répond tout de suite"""
    os.makedirs(path, exist_ok=True)
    os.makedirs(SOUNDCLOUD_STATE_DIR, exist_ok=True)
    threading.Thread(
        target=_run_scdl,
        args=(url, path, _archive_for(url, archive_suffix), extra_args or []),
        daemon=True,
    ).start()
    return {
        "success": True,
        "message": "Téléchargement lancé",
        "destination": path,
    }


def download_song_or_playlist(url: str) -> dict:
    """Lance le téléchargement d'une chanson ou playlist"""
    try:
        return _start_download(url)
    except Exception as e:
        return {
            "success": False,
            "message": f"Erreur: {str(e)}",
            "destination": DESTINATION_FOLDER,
        }


def get_liked() -> list[SoundcloudTrack]:
    user_id = credentials_sv.get().soundcloud_user_id
    access_token = sc_auth_sv.get_or_refresh_sc_token().access_token

    json_data = sc_client.get_playlists(user_id=user_id, access_token=access_token)

    return [SoundcloudPlaylist(**pl) for pl in json_data]


def download_liked() -> dict:
    """Lance le téléchargement des titres likés"""
    try:
        # Récupéré ici (thread de la requête) car cela accède à la base Django
        username = get_username()
        # -f : les likes ("favorites"). Sans ça, scdl prend les titres publiés par le compte
        return _start_download(
            SOUNDCLOUD_BASE_URL + username,
            path=os.path.join(DESTINATION_FOLDER, SOUNDCLOUD_LIKES_FOLDER),
            extra_args=["-f"],
            archive_suffix="-likes",
        )
    except Exception as e:
        return {
            "success": False,
            "message": f"Erreur: {str(e)}",
            "destination": DESTINATION_FOLDER,
        }
