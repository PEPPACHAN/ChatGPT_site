from django.contrib.auth import login
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .models import *


def registration(request):
    return render(request, "registration.html")


def registration_check(request):
    data = Registered_Users.objects
    post_name = request.POST.get("username", "404")
    post_password = request.POST.get("password", "404")

    try:
        data.get(username=post_name)
    except ObjectDoesNotExist:
        if post_password is not '':
            registrate = Registered_Users(username=post_name, password=make_password(post_password))
            registrate.save()

            request.session.clear()
            request.session["id"] = 1
            request.session["username"] = post_name
            login(request, data.get(username=post_name))
            return HttpResponse(f"{request.session.get('username')}<br>"
                                f"{post_password}")
            # return HttpResponseRedirect()
        else:
            return HttpResponse("Forgot password")

    else:
        return HttpResponse("User already exists")
