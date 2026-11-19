from ninja import Router
from ninja.errors import HttpError
from app.services.spotify_auth import SpotifyNotConnected
from app.schemas import SpotifyPlaylist
from app.services import spotify as sp_sv

router = Router()


# /spotify
@router.get("/playlists", response=list[SpotifyPlaylist] | None)
def get_playlists(request):
    try:
        return sp_sv.get_playlists()
    except SpotifyNotConnected as e:
        raise HttpError(401, str(e))

@router.post("/dl-playlist", response=dict)
def download_playlist(request, url: str):
    return sp_sv.download_song_or_playlist(url)
