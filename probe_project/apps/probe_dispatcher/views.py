# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse

from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext

from probe_project.apps.probe_dispatcher.forms import ProbeForm

from probe_project.apps.probe_dispatcher.models import Probe, Sensor




# todo: use decorators to limit views to registered users
# todo: users should only view their probes


def probe_detail(request, id):
    if request.user.is_authenticated():
        probe = Probe.objects.get(id=id)
        if probe.user_id == request.user.id or request.user.is_staff:
            return render_to_response("probe_dispatcher/probe_detail.html", RequestContext(request, {
                'probe': Probe.objects.get(id=id)
            }))
        else:
            return redirect('/')
    else:
        return redirect('/')


def probe_form(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = ProbeForm(request.POST)
            instance = form.save()
            return HttpResponseRedirect(reverse(probe_detail, args=(instance.id,)))
        return render_to_response("probe_dispatcher/probe_form.html", RequestContext(request, {'form': ProbeForm}))


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