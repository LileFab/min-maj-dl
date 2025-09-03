from app.models import Credential, SpotifyAuthInformations
from app.clients.spotify_auth import fetch_client_credentials_token
from django.utils import timezone
from datetime import timedelta
from app.constants import SAFETY_MARGIN


def get() -> SpotifyAuthInformations | None:
    return SpotifyAuthInformations.objects.first()


def get_or_refresh_sp_token() -> SpotifyAuthInformations:
    creds = Credential.objects.first()
    if not creds or not creds.spotify_client_id or not creds.spotify_client_secret:
        raise ValueError("Spotify credentials missing")

    sp = SpotifyAuthInformations.objects.first() or SpotifyAuthInformations()

    # refresh si expiré ou absent
    if not sp.access_token or not sp.expires_at or timezone.now() >= sp.expires_at:
        print("Access token expiré ou absent, requête d'un access token")
        data = fetch_client_credentials_token(
            creds.spotify_client_id, creds.spotify_client_secret
        )
        sp.access_token = data["access_token"]
        sp.token_type = data.get("token_type")
        sp.expires_in = data.get("expires_in", 0)
        sp.expires_at = timezone.now() + timedelta(
            seconds=max(sp.expires_in - SAFETY_MARGIN, 0)
        )
        sp.save()

    return sp
