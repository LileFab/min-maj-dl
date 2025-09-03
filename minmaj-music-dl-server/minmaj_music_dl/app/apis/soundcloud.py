from ninja import Router
from app.schemas import SoundcloudPlaylist
from app.services import soundcloud as sc_sv

router = Router()


# /soundcloud
@router.get("/playlists", response=list[SoundcloudPlaylist] | None)
def get_playlists(request):
    return sc_sv.get_playlists()


@router.get("/liked", response=list[SoundcloudPlaylist] | None)
def get_liked(request):
    return sc_sv.get_playlists()


@router.get("/username", response=str)
def get_username(request):
    return sc_sv.get_username()


@router.post("/dl-playlist", response=dict)
def download_playlist(request, url: str):
    return sc_sv.download_song_or_playlist(url)
