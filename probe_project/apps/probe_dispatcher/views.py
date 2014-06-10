# -*- coding: utf-8 -*-

from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext

from probe_project.apps.probe_dispatcher.models import Probe, Sensor


# todo: use decorators to limit views to registered users
# todo: users should only view their probes

def probes(request):
    if request.user.is_authenticated():
        return render_to_response("probe_dispatcher/probes.html", RequestContext(request, {
            'probes': Probe.objects.all()
        }))
    else:
        return redirect('/')



def sensors(request):
    if request.user.is_authenticated():
        return render_to_response("probe_dispatcher/sensors.html", RequestContext(request, {
            'sensors': Sensor.objects.all()
        }))
    else:
        return redirect('/')


def probe_file(request, id, hash):
    currentProbe = get_object_or_404(Probe, id=id)
    if (currentProbe.hash != hash):
        raise Http404

    for sensor in currentProbe.sensors.all():
        print(sensor.name)

    return render_to_response("probe_dispatcher/probe.html", RequestContext(request, {'id': id, 'hash': hash}),
                              content_type='application/javascript')


def answer(request):
    return render_to_response(request, {}, )


def dashboard(request):
    return render_to_response("probe_dispatcher/dashboard.html", RequestContext(request, {}))