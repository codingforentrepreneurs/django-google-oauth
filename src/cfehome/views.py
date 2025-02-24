from django.http import HttpResponse
# from django.shortcuts import redirect

def google_login_redirect_view(request):
    print(request.GET)
    return HttpResponse("https://google.com redirect")


def google_login_callback_view(request):
    print(request.GET)
    return HttpResponse("Now a user callback")
