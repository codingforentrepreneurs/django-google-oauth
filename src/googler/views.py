from django.http import HttpResponse
from django.shortcuts import redirect

from . import oauth
# 

def google_login_redirect_view(request):
    google_oauth2_url = oauth.generate_auth_url()
    return redirect(google_oauth2_url)


def google_login_callback_view(request):
    print(request.GET)
    return HttpResponse("Now a user callback")