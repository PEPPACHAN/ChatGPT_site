from django.urls import path

from .views import *

urlpatterns = [
    path("registration/", registration, name="reg"),
    path("registration/check/", registration_check, name="reg_check"),
    path("signin/", signin, name="signin"),
    path("signin/check/", signin_check, name="signin_check"),
]
