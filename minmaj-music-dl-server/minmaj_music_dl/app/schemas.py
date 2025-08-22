from app.models import Credential, SoundcloudAuthInformations
from ninja import ModelSchema, Schema


# Credentials
class CredentialSchema(ModelSchema):
    class Meta:
        model = Credential
        fields = (
            "soundcloud_client_id",
            "soundcloud_client_secret",
            "soundcloud_user_id",
            "spotify_client_id",
            "spotify_client_secret",
            "last_update_date",
        )


class AddCredentialSchema(Schema):
    soundcloud_client_id: str | None = None
    soundcloud_client_secret: str | None = None
    soundcloud_user_id: str | None = None
    spotify_client_id: str | None = None
    spotify_client_secret: str | None = None
    last_update_date: str | None = None


# SoundcloudAuthInformations


class SoundcloudAuthInformationsSchema(ModelSchema):
    class Meta:
        model = SoundcloudAuthInformations
        fields = (
            "access_token",
            "token_type",
            "expires_in",
            "refresh_token",
            "scope",
            "expires_at",
        )


class SoundcloudPlaylist(Schema):
    title: str
    permalink_url: str
    duration: int
    track_count: int
    last_modified: str | None

class SoundcloudTrack(Schema):
    title: str
    permalink_url: str
    duration: int
    purchase_title: str | None
    purchase_url: str | None
    genre: str | None
    artwork_url: str| None
