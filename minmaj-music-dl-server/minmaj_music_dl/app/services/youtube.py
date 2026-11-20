import logging
import os
import threading
from datetime import date
from urllib.parse import parse_qs, urlparse

import yt_dlp

from app.constants import DESTINATION_FOLDER, YOUTUBE_FOLDER_PREFIX

logger = logging.getLogger(__name__)

YOUTUBE_HOSTS = {
    "youtube.com",
    "www.youtube.com",
    "m.youtube.com",
    "music.youtube.com",
    "youtu.be",
}


def is_youtube_url(url: str) -> bool:
    parsed = urlparse(url.strip())
    return parsed.scheme in ("http", "https") and parsed.hostname in YOUTUBE_HOSTS


def _is_mix(url: str) -> bool:
    """Les « mix » YouTube (list=RD...) sont générés à l'infini : on ne prend que la vidéo"""
    list_id = parse_qs(urlparse(url).query).get("list", [""])[0]
    return list_id.startswith("RD")


def _ydl_options(path: str, url: str) -> dict:
    return {
        # Meilleur flux audio disponible (en général Opus ~160k, sinon AAC),
        # gardé tel quel : un réencodage (mp3...) ne ferait que perdre en qualité
        "format": "bestaudio/best",
        "outtmpl": os.path.join(path, "%(title)s.%(ext)s"),
        # Noms compatibles Samba / Windows (remplace : ? * etc.)
        "windowsfilenames": True,
        "noplaylist": _is_mix(url),
        "ignoreerrors": True,  # une vidéo indisponible ne bloque pas la playlist
        "writethumbnail": True,
        "quiet": True,
        "no_warnings": True,
        "noprogress": True,
        "postprocessors": [
            # Extrait l'audio du conteneur (webm -> .opus, mp4 -> .m4a) sans réencoder
            {"key": "FFmpegExtractAudio", "preferredcodec": "best"},
            {"key": "FFmpegMetadata", "add_metadata": True},
            # Pochette en jpg (le webp n'est pas accepté par tous les lecteurs)
            {"key": "FFmpegThumbnailsConvertor", "format": "jpg", "when": "before_dl"},
            {"key": "EmbedThumbnail"},
        ],
    }


def _run_ytdlp(url: str, path: str) -> None:
    try:
        with yt_dlp.YoutubeDL(_ydl_options(path, url)) as ydl:
            code = ydl.download([url])
        if code == 0:
            logger.info("Téléchargement YouTube terminé: %s", url)
        else:
            logger.error("yt-dlp a rencontré des erreurs (code %s) pour %s", code, url)
    except Exception:
        logger.exception("Erreur pendant le téléchargement YouTube de %s", url)


def download_video_or_playlist(url: str) -> dict:
    """Lance en arrière-plan le téléchargement audio d'une vidéo / playlist YouTube
    dans /music/yt-AAAA-MM-JJ"""
    path = os.path.join(DESTINATION_FOLDER, f"{YOUTUBE_FOLDER_PREFIX}{date.today().isoformat()}")

    if not is_youtube_url(url):
        return {"success": False, "message": "URL YouTube invalide", "destination": path}

    try:
        os.makedirs(path, exist_ok=True)
        threading.Thread(target=_run_ytdlp, args=(url.strip(), path), daemon=True).start()
        return {"success": True, "message": "Téléchargement lancé", "destination": path}
    except Exception as e:
        return {"success": False, "message": f"Erreur: {str(e)}", "destination": path}
