from ninja import Router
from app.schemas import SpotifyPlaylist
from app.services import spotify as sp_sv

router = Router()


# /spotify
@router.get("/playlists", response=list[SpotifyPlaylist] | None)
def get_playlists(request):
    return sp_sv.get_playlists()

@router.post("/dl-playlist", response=dict)
def download_playlist(request, url: str):
    return sp_sv.download_song_or_playlist(url)
