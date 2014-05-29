# -*- coding: utf-8 -*-
from gettext import gettext as _

from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

from probe_dispatcher import views


def home(request):
    return render_to_response("home.jinja2", RequestContext(request, {'app': 'Probe'}))


@csrf_protect
def login(request):
    if request.POST:
        user = authenticate(username=request.POST.get('UsernameEmail'), password=request.POST.get('password'))
        if user is not None:
            if user.is_active:
                return redirect(reverse(views.dashboard), context_instance=RequestContext(request, {
                'message': 'Welcome to your new account'}))
        else:
            return render_to_response("login.jinja2",
                                      RequestContext(request, {'message': _('Invalid user or password')}))

    else:
        return render_to_response("login.jinja2", RequestContext(request, {}))


@csrf_protect
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return reverse(views.dashboard)
    else:
        form = UserCreationForm()
    return render_to_response("registration/register-form.jinja2", RequestContext(request, {'form': form, }))


def logout(request):
    logout(request)
    return None
