import datetime
from django.utils import timezone
from .social_auth_imports import (
    SocialAccount,
    SocialApp,
    SocialToken,
)

def get_google_app_provider(provider="google"):
    lookups = {"provider": provider}
    try:
        return SocialApp.objects.get(**lookups)
    except (SocialApp.MultipleObjectsReturned, SocialApp.DoesNotExist):
        return SocialApp.objects.filter(provider="google").first()


def save_google_auth_tokens(user, id_info, token_json):
    provider="google"
    social_app = get_google_app_provider(provider)
    expires_in = token_json.get("expires_in")
    social_account, _ = SocialAccount.objects.get_or_create(
        user=user,
        provider=provider,
        defaults={"uid": id_info["sub"], "extra_data": id_info},
    )
    expires_at = None
    if expires_in:
        expires_at = timezone.now() + datetime.timedelta(seconds=int(expires_in))

    refresh_token = token_json.get("refresh_token", "")
    access_token = token_json["access_token"]
    SocialToken.objects.update_or_create(
        account=social_account,
        app=social_app,
        defaults={
            "token": access_token,
            "token_secret": refresh_token,
            "expires_at": expires_at,
        },
    )