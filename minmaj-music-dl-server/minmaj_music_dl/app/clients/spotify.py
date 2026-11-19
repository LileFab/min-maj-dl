from app.constants import SPOTIFY_ME_PLAYLISTS_URL
from requests import get


def get_playlists(access_token: str):
    """Playlists de l'utilisateur connecté (toutes les pages)"""
    playlists = []
    url = SPOTIFY_ME_PLAYLISTS_URL
    while url:
        resp = get(url, headers={"Authorization": f"Bearer {access_token}"}, timeout=15)
        resp.raise_for_status()
        data = resp.json()

        for pl in data.get("items", []):
            if not pl:
                continue
            # Le compteur de titres s'appelle "tracks" ou "items" selon la version de l'API
            counter = pl.get("items") or pl.get("tracks") or {}
            playlists.append(
                {
                    "name": pl.get("name") or "",
                    "dl_url": pl["external_urls"]["spotify"],
                    "track_count": counter.get("total", 0) if isinstance(counter, dict) else 0,
                    "owner": (pl.get("owner") or {}).get("display_name") or "",
                }
            )
        url = data.get("next")
    return playlists
