import os
from subprocess import run
from app.services import credentials as credentials_sv
from app.services import soundcloud_auth as sc_auth_sv
from app.schemas import SoundcloudPlaylist, SoundcloudTrack
from app.clients import soundcloud as sc_client
from app.constants import DESTINATION_FOLDER, SOUNDCLOUD_BASE_URL


def get_playlists() -> list[SoundcloudPlaylist]:
    user_id = credentials_sv.get().soundcloud_user_id
    access_token = sc_auth_sv.get_or_refresh_sc_token().access_token

    json_data = sc_client.get_playlists(user_id=user_id, access_token=access_token)

    return [SoundcloudPlaylist(**pl) for pl in json_data]


def get_username() -> str:
    user_id = credentials_sv.get().soundcloud_user_id
    access_token = sc_auth_sv.get_or_refresh_sc_token().access_token

    return sc_client.get_username(user_id=user_id, access_token=access_token)


def download_song_or_playlist(url: str) -> dict:
    """Télécharge une chanson ou playlist et retourne le statut"""
    try:
        # Créer le dossier de destination
        os.makedirs(DESTINATION_FOLDER, exist_ok=True)

        # Lancer le téléchargement
        result = run(["scdl", "-l", url, "--path", DESTINATION_FOLDER, "--onlymp3", "--original-name", "--addtofile"], check=True)

        if result.returncode == 0:
            return {
                "success": True,
                "message": "Téléchargement terminé avec succès",
                "destination": DESTINATION_FOLDER,
            }
        else:
            return {
                "success": False,
                "message": f"Erreur lors du téléchargement (code: {result})",
                "destination": DESTINATION_FOLDER,
            }

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
    """Télécharge les titres likés"""
    try:
        # Créer le dossier de destination
        os.makedirs(DESTINATION_FOLDER, exist_ok=True)

        username = get_username()
        url = SOUNDCLOUD_BASE_URL + username

        # Lancer le téléchargement
        result = run(["scdl", "-l", url, "--path", DESTINATION_FOLDER, "--onlymp3", "--original-name", "--addtofile"], check=True)

        if result.returncode == 0:
            return {
                "success": True,
                "message": "Téléchargement terminé avec succès",
                "destination": DESTINATION_FOLDER,
            }
        else:
            return {
                "success": False,
                "message": f"Erreur lors du téléchargement (code: {result})",
                "destination": DESTINATION_FOLDER,
            }

    except Exception as e:
        return {
            "success": False,
            "message": f"Erreur: {str(e)}",
            "destination": DESTINATION_FOLDER,
        }