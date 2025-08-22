from ninja import NinjaAPI
from app.apis.credentials import router as credentials_router
from app.apis.souncloud_auth import router as sc_auth_router
from app.apis.soundcloud import router as sc_router


api = NinjaAPI(title="MusicDL API", version="0.1.0")

# Monte le sous-ensemble de routes "credentials" sous /api/credentials/...
api.add_router("/credentials", credentials_router, tags=["credentials"])
api.add_router("/sc_auth_infos", sc_auth_router, tags=["sc_auth_infos"])
api.add_router("/soundcloud", sc_router, tags=["soundcloud"])
