import logging

logger = logging.getLogger(__name__)

class SocialAccount:
    objects = None
    
    def __init__(self, user=None, provider=None, uid=None, extra_data=None):
        self.user = user
        self.provider = provider
        self.uid = uid
        self.extra_data = extra_data

class SocialApp:
    objects = None
    
    def __init__(self, provider=None):
        self.provider = provider

class SocialToken:
    objects = None
    
    def __init__(self, account=None, app=None, token=None, token_secret=None, expires_at=None):
        self.account = account
        self.app = app
        self.token = token
        self.token_secret = token_secret
        self.expires_at = expires_at

try:
    from allauth.socialaccount.models import (
        SocialAccount, 
        SocialApp, 
        SocialToken
    )
except ImportError:
    logger.warning("allauth not installed") 