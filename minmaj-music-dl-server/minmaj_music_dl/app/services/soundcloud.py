import os
from subprocess import call
from app.services import credentials as credentials_sv
from app.services import soundcloud_auth as sc_auth_sv
from app.schemas import SoundcloudPlaylist
from app.clients import soundcloud as sc_client
from app.constants import DESTINATION_FOLDER

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
        result = call(f'scdl -l "{url}" --path "{DESTINATION_FOLDER}"', shell=True)
        
        if result == 0:
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