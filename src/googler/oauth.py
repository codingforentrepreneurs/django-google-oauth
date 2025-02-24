from urllib.parse import urljoin, urlencode
from django.conf import settings

from . import security

def get_google_oauth_callback_url(drop_https=False, force_https=False):
    url =  urljoin(settings.BASE_URL, settings.GOOGLE_AUTH_CALLBACK_PATH)
    if drop_https:
        url = url.replace("https://", "http://")
    if force_https:
        url = url.replace("http://", "https://")
    return url


def generate_auth_url():
    redirect_uri = get_google_oauth_callback_url()
    # public state item
    state = security.generate_state()

    # private, public
    code_verifier, code_challenge = security.generate_pkce_pair()

    # google cloud auth platform client id
    google_auth_client_id = None

    scope = " ".join([
        "openid",
        "email", 
        "profile"
    ])

    auth_params = {
        "client_id": google_auth_client_id,
        "redirect_uri": redirect_uri, 
        "response_type": "code",
        "scope": scope,
        "state": state,
        "code_challenge": code_challenge,
        "code_challenge_method": "S256",
        "access_type": "offline",
    }
    encoded_params = urlencode(auth_params)
    google_oauth_url = "https://accounts.google.com/o/oauth2/v2/auth"
    return urljoin(google_oauth_url, f"?{encoded_params}")