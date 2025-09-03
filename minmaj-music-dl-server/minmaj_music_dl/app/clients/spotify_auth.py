from requests import post
from app.constants import SP_API_AUTH_URL


def fetch_client_credentials_token(client_id: str, client_secret: str) -> dict:
    headers = {
        "Accept": "application/json; charset=utf-8",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = {
        "grant_type": "client_credentials",
        "client_id": {client_id},
        "client_secret": {client_secret},
    }
    resp = post(SP_API_AUTH_URL, headers=headers, data=data, timeout=15)
    resp.raise_for_status()
    return resp.json()  # {access_token, token_type, expires_in}
