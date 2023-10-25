from django.urls import path

from .views import *

urlpatterns = [
    path("registration/", registration, name="reg"),
    path("registration/check/", registration_check, name="reg_check")
]
