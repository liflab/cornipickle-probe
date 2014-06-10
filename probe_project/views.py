# -*- coding: utf-8 -*-
from gettext import gettext as _

from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from userena.forms import AuthenticationForm

from probe_project.apps.probe_dispatcher import views


@csrf_protect
def home(request):
    if request.user.is_active:
        return redirect(views.dashboard)
    else:
        return render_to_response("home.html", RequestContext(request, {'app': 'Probe', 'form': AuthenticationForm}))


@csrf_protect
def custom_login(request):
    if request.POST:
        user = authenticate(username=request.POST.get('UsernameEmail'), password=request.POST.get('password'))
        if user is not None:
            if user.is_active:
                return redirect(reverse(views.dashboard),
                                context_instance=RequestContext(request, {'message': 'Welcome back!'}))
            else:
                return render_to_response("login.html", RequestContext(request, {
                'error': _('User has been disabled, please contact us for more details')}))
        else:
            return render_to_response("login.html", RequestContext(request, {'error': _('Invalid user or password')}))

    else:
        return render_to_response("login.html", RequestContext(request, {}))


@csrf_protect
def custom_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            if ("terms_and_conditions" in request.POST):
                new_user = form.save()
                return redirect(reverse(views.dashboard), {'message': _('Welcome to your new account!')})
            else:
                return render_to_response("register.html", RequestContext(request, {'form': form, 'terms_error': _(
                    "You must accept the terms and conditions")}))

    else:
        form = UserCreationForm()
    return render_to_response("register.html", RequestContext(request, {'form': form}))


def custom_logout(request, next_page):
    logout(request)
    return redirect(next_page)
