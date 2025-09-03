from app.models import Credential, SoundcloudAuthInformations, SpotifyAuthInformations
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
            "spotify_user_id",
            "last_update_date",
        )


class AddCredentialSchema(Schema):
    soundcloud_client_id: str | None = None
    soundcloud_client_secret: str | None = None
    soundcloud_user_id: str | None = None
    spotify_client_id: str | None = None
    spotify_client_secret: str | None = None
    spotify_user_id: str | None = None
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


# SpotifyAuthInformations


class SpotifyAuthInformationsSchema(ModelSchema):
    class Meta:
        model = SpotifyAuthInformations
        fields = (
            "access_token",
            "token_type",
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
    artwork_url: str | None


class SpotifyPlaylist(Schema):
    name: str
    dl_url: str
    track_count: int
    owner: str
