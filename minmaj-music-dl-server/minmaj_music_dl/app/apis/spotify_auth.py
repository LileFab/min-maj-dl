from django.http import HttpResponse
from django.utils.html import escape
from ninja import Router
from ninja.errors import HttpError
from app.constants import SPOTIFY_REDIRECT_URI
from app.services import spotify_auth as sp_auth_sv

router = Router()


# /sp_auth_infos
@router.get("/status", response=dict)
def status(request):
    return {"connected": sp_auth_sv.is_connected(), "redirect_uri": SPOTIFY_REDIRECT_URI}


@router.get("/login-url", response=dict)
def login_url(request):
    try:
        return {"url": sp_auth_sv.get_login_url(), "redirect_uri": SPOTIFY_REDIRECT_URI}
    except ValueError as e:
        raise HttpError(400, str(e))


@router.post("/connect", response=dict)
def connect(request, code: str):
    """`code` : le code OAuth ou l'URL complète de redirection collée par l'utilisateur"""
    try:
        sp_auth_sv.connect(code)
        return {"success": True, "message": "Compte Spotify connecté"}
    except ValueError as e:
        raise HttpError(400, str(e))


@router.get("/callback")
def callback(request, code: str = "", error: str = ""):
    """Utilisé si SPOTIFY_REDIRECT_URI pointe directement sur ce backend (ex. via un tunnel HTTPS)"""
    try:
        sp_auth_sv.connect(f"?code={code}" if code else f"?error={error or 'inconnue'}")
        return HttpResponse("<p>Compte Spotify connecté. Tu peux fermer cet onglet.</p>")
    except ValueError as e:
        return HttpResponse(f"<p>Échec de la connexion Spotify : {escape(str(e))}</p>", status=400)


@router.post("/disconnect", response=dict)
def disconnect(request):
    sp_auth_sv.disconnect()
    return {"success": True}
