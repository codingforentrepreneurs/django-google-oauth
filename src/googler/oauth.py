from urllib.parse import urljoin
from django.conf import settings

def get_google_oauth_callback_url(drop_https=False, force_https=False):
    url =  urljoin(settings.BASE_URL, settings.GOOGLE_AUTH_CALLBACK_PATH)
    if drop_https:
        url = url.replace("https://", "http://")
    if force_https:
        url = url.replace("http://", "https://")
    return url


