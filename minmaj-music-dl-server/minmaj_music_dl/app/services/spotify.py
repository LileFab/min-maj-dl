import os
from subprocess import run
from app.services import credentials as credentials_sv
from app.services import spotify_auth as sp_auth_sv
from app.schemas import SpotifyPlaylist, SpotifyAuthInformations
from app.clients import spotify as sp_client
from app.constants import DESTINATION_FOLDER

def get_playlists() -> list[SpotifyPlaylist]:
    user_id = credentials_sv.get().spotify_user_id
    access_token = sp_auth_sv.get_or_refresh_sp_token().access_token

    json_data = sp_client.get_playlists(user_id=user_id, access_token=access_token)
    
    return [SpotifyPlaylist(**pl) for pl in json_data]

def download_song_or_playlist(url: str) -> dict:
    """Télécharge une chanson ou playlist et retourne le statut"""
    try:
        # Créer le dossier de destination
        os.makedirs(DESTINATION_FOLDER, exist_ok=True)

        access_token = sp_auth_sv.get_or_refresh_sp_token().access_token
        
        # Lancer le téléchargement
        result = run(
        [
            "spotdl", "download", url,
            "--format", "mp3",
            "--bitrate", "320k",
            "--threads", "4",
            "--auth-token", access_token,
            "--output", f"{DESTINATION_FOLDER}/{{list-name}}/{{artists}} - {{title}}.{{output-ext}}",
        ],
        check=True
    )
        
        if result.returncode == 0:
            return {
                "success": True,
                "message": "Téléchargement terminé avec succès",
                "destination": DESTINATION_FOLDER
            }
        else:
            return {
                "success": False,
                "message": f"Erreur lors du téléchargement (code: {result})",
                "destination": DESTINATION_FOLDER
            }
            
    except Exception as e:
        return {
            "success": False,
            "message": f"Erreur: {str(e)}",
            "destination": DESTINATION_FOLDER
        }