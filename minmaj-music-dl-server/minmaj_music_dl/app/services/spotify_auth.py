from datetime import timedelta
from urllib.parse import urlencode, urlparse, parse_qs

from django.utils import timezone

from app.clients.spotify_auth import exchange_code, refresh_user_token
from app.constants import SAFETY_MARGIN, SP_AUTHORIZE_URL, SP_SCOPES, SPOTIFY_REDIRECT_URI
from app.models import Credential, SpotifyAuthInformations


class SpotifyNotConnected(Exception):
    pass


def get() -> SpotifyAuthInformations | None:
    return SpotifyAuthInformations.objects.first()


def _get_app_credentials() -> Credential:
    creds = Credential.objects.first()
    if not creds or not creds.spotify_client_id or not creds.spotify_client_secret:
        raise ValueError("Client ID / Client Secret Spotify manquants : sauvegarde-les d'abord")
    return creds


def is_connected() -> bool:
    sp = get()
    return bool(sp and sp.refresh_token)


def get_login_url() -> str:
    creds = _get_app_credentials()
    params = {
        "client_id": creds.spotify_client_id,
        "response_type": "code",
        "redirect_uri": SPOTIFY_REDIRECT_URI,
        "scope": SP_SCOPES,
        "show_dialog": "true",
    }
    return f"{SP_AUTHORIZE_URL}?{urlencode(params)}"


def _save_tokens(sp: SpotifyAuthInformations, data: dict) -> SpotifyAuthInformations:
    sp.access_token = data["access_token"]
    sp.token_type = data.get("token_type")
    sp.expires_in = data.get("expires_in", 0)
    sp.expires_at = timezone.now() + timedelta(seconds=max(sp.expires_in - SAFETY_MARGIN, 0))
    # Spotify ne renvoie pas toujours un nouveau refresh_token : on garde l'ancien
    if data.get("refresh_token"):
        sp.refresh_token = data["refresh_token"]
    if data.get("scope"):
        sp.scope = data["scope"]
    sp.save()
    return sp


def connect(code_or_url: str) -> SpotifyAuthInformations:
    """Accepte le code OAuth, ou l'URL complète vers laquelle Spotify a redirigé"""
    value = code_or_url.strip()
    if "code=" in value or "error=" in value:
        query = parse_qs(urlparse(value).query)
        if "error" in query:
            raise ValueError(f"Connexion Spotify refusée : {query['error'][0]}")
        value = query.get("code", [""])[0]
    if not value:
        raise ValueError("Aucun code trouvé dans l'URL collée")

    creds = _get_app_credentials()
    data = exchange_code(creds.spotify_client_id, creds.spotify_client_secret, value, SPOTIFY_REDIRECT_URI)
    return _save_tokens(get() or SpotifyAuthInformations(), data)


def disconnect() -> None:
    SpotifyAuthInformations.objects.all().delete()


def get_or_refresh_sp_token() -> SpotifyAuthInformations:
    """Token utilisateur valide, renouvelé via le refresh_token si besoin"""
    sp = get()
    if not sp or not sp.refresh_token:
        raise SpotifyNotConnected(
            "Compte Spotify non connecté : clique sur « Connecter Spotify » dans Credentials"
        )

    if not sp.access_token or not sp.expires_at or timezone.now() >= sp.expires_at:
        creds = _get_app_credentials()
        data = refresh_user_token(creds.spotify_client_id, creds.spotify_client_secret, sp.refresh_token)
        _save_tokens(sp, data)

    return sp
