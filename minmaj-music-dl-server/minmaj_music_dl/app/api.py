from ninja import NinjaAPI
from app.apis.credentials import router as credentials_router
from app.apis.souncloud_auth import router as sc_auth_router
from app.apis.spotify_auth import router as sp_auth_router
from app.apis.soundcloud import router as sc_router
from app.apis.spotify import router as sp_router


api = NinjaAPI(title="MusicDL API", version="0.1.0")

# Monte le sous-ensemble de routes "credentials" sous /api/credentials/...
api.add_router("/credentials", credentials_router, tags=["credentials"])
api.add_router("/sc_auth_infos", sc_auth_router, tags=["sc_auth_infos"])
api.add_router("/sp_auth_infos", sp_auth_router, tags=["sp_auth_infos"])
api.add_router("/soundcloud", sc_router, tags=["soundcloud"])
api.add_router("/spotify", sp_router, tags=["spotify"])