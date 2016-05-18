# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import logout
from userena.forms import AuthenticationForm

from probe_project.apps.probe_dispatcher import views


@csrf_protect
def home(request):
    if request.user.is_active:
        return redirect(views.dashboard)
    else:
        return render_to_response("home.html", RequestContext(request, {'app': 'Probe', 'form': AuthenticationForm}))


def custom_logout(request, next_page):
    logout(request)
    return redirect(next_page)
