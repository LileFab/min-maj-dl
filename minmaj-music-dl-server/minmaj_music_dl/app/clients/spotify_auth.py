from requests import post
from app.constants import SP_API_AUTH_URL


def _token_request(client_id: str, client_secret: str, data: dict) -> dict:
    resp = post(
        SP_API_AUTH_URL,
        auth=(client_id, client_secret),
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data=data,
        timeout=15,
    )
    if not resp.ok:
        raise ValueError(f"Spotify a refusé la requête de token ({resp.status_code}): {resp.text}")
    return resp.json()


def exchange_code(client_id: str, client_secret: str, code: str, redirect_uri: str) -> dict:
    """Échange le code OAuth contre {access_token, refresh_token, expires_in, scope, ...}"""
    return _token_request(
        client_id,
        client_secret,
        {"grant_type": "authorization_code", "code": code, "redirect_uri": redirect_uri},
    )


def refresh_user_token(client_id: str, client_secret: str, refresh_token: str) -> dict:
    """Renouvelle le token utilisateur (le refresh_token n'est pas toujours renvoyé)"""
    return _token_request(
        client_id,
        client_secret,
        {"grant_type": "refresh_token", "refresh_token": refresh_token},
    )
