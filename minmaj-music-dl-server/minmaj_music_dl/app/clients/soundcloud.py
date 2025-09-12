from app.constants import (
    SOUNDCLOUD_USER_BASE,
    SOUNDCLOUD_PLAYLIST_START_URL,
    SOUNDCLOUD_PLAYLIST_END_URL,
    SOUNDCLOUD_LIKES_END_URL
)
from requests import get


def get_playlists(user_id: int, access_token: str):
    url = f"{SOUNDCLOUD_PLAYLIST_START_URL}{SOUNDCLOUD_USER_BASE}{user_id}{SOUNDCLOUD_LIKES_END_URL}"
    resp = get(url, headers={"Authorization": f"Bearer {access_token}"}, timeout=15)
    resp.raise_for_status()
    data = resp.json()

    items = data.get("collection", data if isinstance(data, list) else [])

    urns = [
        {
            "title": pl.get("title"),
            "permalink_url": pl.get("permalink_url"),
            "duration": pl.get("duration"),
            "track_count": pl.get("track_count"),
            "last_modified": pl.get("last_modified"),
        }
        for pl in items
    ]
    return urns


def get_username(user_id: int, access_token: str):
    url = f"{SOUNDCLOUD_PLAYLIST_START_URL}{SOUNDCLOUD_USER_BASE}{str(user_id)}"
    resp = get(url, headers={"Authorization": f"Bearer {access_token}"}, timeout=15)

    resp.raise_for_status()
    data = resp.json()

    return data["permalink"]

def get_likes(user_id: int, access_token: str):
    url = f"{SOUNDCLOUD_PLAYLIST_START_URL}{SOUNDCLOUD_USER_BASE}{user_id}{SOUNDCLOUD_LIKES_END_URL}"
    resp = get(url, headers={"Authorization": f"Bearer {access_token}"}, timeout=15)
    resp.raise_for_status()
    data = resp.json()

    items = data.get("collection", data if isinstance(data, list) else [])

    urns = [
        {
            "title": pl.get("title"),
            "permalink_url": pl.get("permalink_url"),
            "duration": pl.get("duration"),
            "purchase_title": pl.get("purchase_title"),
            "purchase_url": pl.get("purchase_url"),
            "genre": pl.get("genre"),
            "artwork_url": pl.get("artwork_url")
        }
        for pl in items
    ]
    return urns