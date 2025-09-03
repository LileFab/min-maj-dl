from ninja import Router
from app.schemas import SoundcloudAuthInformationsSchema
from app.services import soundcloud_auth as sc_auth_sv

router = Router()


# /sc_auth_infos
@router.get("/", response=SoundcloudAuthInformationsSchema | None)
def get_sc_auth_infos(request):
    return sc_auth_sv.get()


@router.get("/authentificate", response=SoundcloudAuthInformationsSchema)
def authentificate(request):
    return sc_auth_sv.get_or_refresh_sc_token()
