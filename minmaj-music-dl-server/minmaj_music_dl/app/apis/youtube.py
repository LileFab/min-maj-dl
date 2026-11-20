from ninja import Router
from app.services import youtube as yt_sv

router = Router()


# /youtube
@router.post("/dl", response=dict)
def download(request, url: str):
    return yt_sv.download_video_or_playlist(url)
