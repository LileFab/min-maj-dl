from ninja import Router
from app.schemas import SpotifyAuthInformationsSchema
from app.services import spotify_auth as sp_auth_sv

router = Router()


# /sc_auth_infos
@router.get("/", response=SpotifyAuthInformationsSchema | None)
def get_sc_auth_infos(request):
    return sp_auth_sv.get()


@router.get("/authentificate", response=SpotifyAuthInformationsSchema)
def authentificate(request):
    return sp_auth_sv.get_or_refresh_sp_token()
