from .authenticate_abstract import Auth
from django.contrib.auth import authenticate as django_auth, login as django_login, logout as dj_logout
from django.http.request import HttpRequest
from ..backends.email_backend import EmailBackend

class AppDjangoAuth(Auth):
    """ a type of auth, implements the default django_auth """
    
    def authenticate(self, request: HttpRequest, email: str, password: str)-> bool:
        user_auth = django_auth(request=request, email=email, password=password)
        if user_auth is not None:
            django_login(request=request, user=user_auth)
            return user_auth
        
        return None

    def logout(self, request: HttpRequest,  user=None, *args, **kwargs):
        dj_logout(request=request)
        
            


