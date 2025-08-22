from django.db import models
from django.utils import timezone
from datetime import timedelta
from app.constants import SAFETY_MARGIN


class Credential(models.Model):
    soundcloud_client_id = models.CharField(max_length=200, null=True, blank=True)
    soundcloud_client_secret = models.CharField(max_length=200, null=True, blank=True)
    soundcloud_user_id = models.IntegerField(null=True, blank=True)
    spotify_client_id = models.CharField(max_length=200, null=True, blank=True)
    spotify_client_secret = models.CharField(max_length=200, null=True, blank=True)
    last_update_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return super().__str__()


class SoundcloudAuthInformations(models.Model):
    access_token = models.CharField(null=True, blank=True)
    token_type = models.CharField(null=True, blank=True)
    expires_in = models.IntegerField(null=True, blank=True)
    expires_at = models.DateTimeField(null=True, blank=True)
    refresh_token = models.CharField(null=True, blank=True)
    scope = models.CharField(null=True, blank=True)

    def set_tokens(self, data: dict):
        """Enregistre les infos reçues de SoundCloud et calcule expire_at."""
        self.access_token = data["access_token"]
        self.token_type = data["token_type"]
        self.expires_in = data["expires_in"]
        self.refresh_token = data.get("refresh_token")
        self.scope = data.get("scope", "")
        self.expires_at = timezone.now() + timedelta(
            seconds=self.expires_in - SAFETY_MARGIN
        )
        self.save()

    def is_expired(self) -> bool:
        """Retourne True si le token est déjà expiré."""
        return not self.expires_at or timezone.now() >= self.expires_at
