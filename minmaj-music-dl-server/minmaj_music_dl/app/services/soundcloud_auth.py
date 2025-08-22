from app.models import SoundcloudAuthInformations, Credential
from app.clients.soundcloud_auth import fetch_client_credentials_token
from django.utils import timezone
from datetime import timedelta
from app.constants import SAFETY_MARGIN


def get() -> SoundcloudAuthInformations | None:
    return SoundcloudAuthInformations.objects.first()


def get_or_refresh_sc_token() -> SoundcloudAuthInformations:
    creds = Credential.objects.first()
    if (
        not creds
        or not creds.soundcloud_client_id
        or not creds.soundcloud_client_secret
    ):
        raise ValueError("SoundCloud credentials missing")

    sc = SoundcloudAuthInformations.objects.first() or SoundcloudAuthInformations()

    # refresh si expiré ou absent
    if not sc.access_token or not sc.expires_at or timezone.now() >= sc.expires_at:
        print("Access token expiré ou absent, requête d'un access token")
        data = fetch_client_credentials_token(
            creds.soundcloud_client_id, creds.soundcloud_client_secret
        )
        sc.access_token = data["access_token"]
        sc.token_type = data.get("token_type")
        sc.expires_in = data.get("expires_in", 0)
        sc.refresh_token = data.get("refresh_token")
        sc.scope = data.get("scope", "")
        sc.expires_at = timezone.now() + timedelta(
            seconds=max(sc.expires_in - SAFETY_MARGIN, 0)
        )
        sc.save()

    return sc
