from django.conf import settings
from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import redirect, render

from . import oauth, services

LOGIN_REDIRECT_URL = settings.LOGIN_REDIRECT_URL
# 

def google_login_view(request):
    if request.method == "POST":
        # csrf_token security
        google_oauth2_url = oauth.generate_auth_url()
        return redirect(google_oauth2_url)
    return render(request, "googler/login.html", {})


def google_login_callback_view(request):
    # print(request.GET)
    state = request.GET.get('state')
    code = request.GET.get('code')
    try:
        token_json = oauth.verify_google_oauth_callback(state, code)
    except Exception as e:
        return HttpResponse(f"{e}", status=400)
    google_user_info = oauth.verify_token_json(token_json)
    user = services.get_or_create_google_user(google_user_info)
    # save_google_auth_tokens(user, google_user_info, token_json)
    login(request, user)
    return redirect(LOGIN_REDIRECT_URL)

