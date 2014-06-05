# -*- coding: utf-8 -*-
from gettext import gettext as _

from django.core.urlresolvers import reverse
from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext

from probe_project.apps.probe_dispatcher.models import Probe
import probe_project


def probes(request):
    if request.user.is_authenticated():
        return render_to_response("probe_dispatcher/probes.html", RequestContext(request, {
            'probes': Probe.objects.all()
        }))
    else:
        return redirect(reverse(probe_project.views.custom_login),
                        {'message': _('You are not connected, please, connect first to view this page')})


def probe_file(request, id, hash):
    currentProbe = get_object_or_404(Probe, id=id)
    if (currentProbe.hash != hash):
        raise Http404

    for sensor in currentProbe.sensors.all():
        print(sensor.name)
        pass

    return render_to_response("probe_dispatcher/probe.html", RequestContext(request, {'id': id, 'hash': hash}),
                              content_type='application/javascript')


def answer(request):
    return render_to_response(request, {}, )


def dashboard(request):
    return render_to_response("probe_dispatcher/dashboard.html", RequestContext(request, {}))