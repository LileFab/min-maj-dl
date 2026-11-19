import os

# SC Auth
SC_API_AUTH_URL = "https://secure.soundcloud.com/oauth/token"

# SP auth
SP_API_AUTH_URL = "https://accounts.spotify.com/api/token"
SP_AUTHORIZE_URL = "https://accounts.spotify.com/authorize"
SP_SCOPES = "playlist-read-private playlist-read-collaborative"
# Doit être déclarée à l'identique dans l'app Spotify (developer.spotify.com)
SPOTIFY_REDIRECT_URI = os.environ.get(
    "SPOTIFY_REDIRECT_URI", "http://127.0.0.1:8888/callback"
)

# Auth
SAFETY_MARGIN = 90

# SC
SOUNDCLOUD_PLAYLIST_START_URL = "https://api.soundcloud.com/users/"
SOUNDCLOUD_PLAYLIST_END_URL = "/playlists?access=playable%2Cpreview&show_tracks=false&limit=50&linked_partitioning=true"
SOUNDCLOUD_LIKES_END_URL = "/likes/tracks?access=playable%2Cpreview&limit=50&linked_partitioning=false"
SOUNDCLOUD_USER_BASE = "soundcloud:users:"
SOUNDCLOUD_BASE_URL = "https://soundcloud.com/"

# SP
SPOTIFY_ME_PLAYLISTS_URL = "https://api.spotify.com/v1/me/playlists?limit=50"

# Common
DESTINATION_FOLDER = "/music"  # A changer
# Pistes déjà téléchargées, ignorées aux relances
SCDL_ARCHIVE_FILE = f"{DESTINATION_FOLDER}/.scdl-archive.txt"
# Archive + nom de dossier par playlist Spotify
SPOTIFY_STATE_DIR = f"{DESTINATION_FOLDER}/.minmaj/spotify"
