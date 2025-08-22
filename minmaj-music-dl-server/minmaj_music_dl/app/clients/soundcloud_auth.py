# clients/soundcloud.py (client HTTP)
from base64 import b64encode
from requests import post
from app.constants import API_AUTH_URL


def fetch_client_credentials_token(client_id: str, client_secret: str) -> dict:
    creds = f"{client_id}:{client_secret}"
    headers = {
        "Accept": "application/json; charset=utf-8",
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": f"Basic {b64encode(creds.encode()).decode()}",
    }
    data = {"grant_type": "client_credentials"}
    resp = post(API_AUTH_URL, headers=headers, data=data, timeout=15)
    resp.raise_for_status()
    return resp.json()  # {access_token, token_type, expires_in, refresh_token?, scope}
