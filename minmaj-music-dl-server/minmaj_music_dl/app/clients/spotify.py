from app.constants import SPOTIFY_PLAYLIST_START_URL, SPOTIFY_PLAYLIST_END_URL
from requests import get


def get_playlists(user_id: int, access_token: str):
    url = f"{SPOTIFY_PLAYLIST_START_URL}{user_id}{SPOTIFY_PLAYLIST_END_URL}"
    resp = get(url, headers={"Authorization": f"Bearer {access_token}"}, timeout=15)
    resp.raise_for_status()
    data = resp.json()

    items = data.get("items", data if isinstance(data, list) else [])

    urns = [
        {
            "name": pl.get("name"),
            "dl_url": pl["external_urls"]["spotify"],
            "track_count": pl["tracks"]["total"],
            "owner": pl["owner"]["display_name"],
        }
        for pl in items
    ]
    return urns
