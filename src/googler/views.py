from django.http import HttpResponse
from django.shortcuts import redirect

from . import oauth, services
# 

def google_login_redirect_view(request):
    google_oauth2_url = oauth.generate_auth_url()
    return redirect(google_oauth2_url)


def google_login_callback_view(request):
    # print(request.GET)
    state = request.GET.get('state')
    code = request.GET.get('code')
    try:
        token_json = oauth.verify_google_oauth_callback(state, code)
    except Exception as e:
        return HttpResponse(f"{e}", status=400)
    # print(token_json)
    google_user_info = oauth.verify_token_json(token_json)
    user = services.get_or_create_google_user(google_user_info)
    print(user)
    return HttpResponse("Now a user callback")

