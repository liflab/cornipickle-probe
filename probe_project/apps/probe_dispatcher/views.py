# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext

from probe_project.apps.probe_dispatcher.forms import ProbeFrontendForm
from probe_project.apps.probe_dispatcher.models import Probe, Sensor


@login_required
def probe_detail(request, probe_id):
    current_probe = get_object_or_404(Probe, id=probe_id)
    if current_probe.user_id == request.user.id or request.user.is_staff:
        return render_to_response("probe_dispatcher/probe_detail.html", RequestContext(request, {
            'probe': current_probe
        }))
    else:
        return redirect('/')


@login_required
def probe_form(request):
    if request.method == 'POST':
        form = ProbeFrontendForm(request.POST)
        form.user = request.user
        if form.is_valid():
            instance = form.save()
            return HttpResponseRedirect(reverse(probe_detail, args=(instance.id,)))
        else:
            return render_to_response("probe_dispatcher/probe_form.html", RequestContext(request, {'form': form}))
    return render_to_response("probe_dispatcher/probe_form.html", RequestContext(request, {'form': ProbeFrontendForm}))


@login_required
def probes(request):
    if request.user.is_authenticated():
        return render_to_response("probe_dispatcher/probes.html", RequestContext(request, {
            'probes': Probe.objects.filter(user=request.user)
        }))
    else:
        return redirect('/')


@login_required
def sensors(request):
    if request.user.is_authenticated():
        return render_to_response("probe_dispatcher/sensors.html", RequestContext(request, {
            'sensors': Sensor.objects.all()
        }))
    else:
        return redirect('/')


def probe_file(request, probe_id, probe_hash, banner=True):
    current_probe = get_object_or_404(Probe, id=probe_id)
    if current_probe.hash != probe_hash:
        raise Http404

    for sensor in current_probe.sensors.all():
        print(sensor.name)

    return render_to_response(
        "probe_dispatcher/probe.js",
        RequestContext(
            request, {
                'id': probe_id,
                'hash': probe_hash,
                'banner': banner,
                'site_url': request.get_host()
            }
        ),
        content_type='application/javascript'
    )


def probe_test(request, probe_id, probe_hash):
    current_probe = get_object_or_404(Probe, id=probe_id)
    if current_probe.hash != probe_hash:
        raise Http404

    for sensor in current_probe.sensors.all():
        print(sensor.name)

    return render_to_response(
        "probe_dispatcher/test.html",
        RequestContext(
            request, {
                'script': current_probe.get_script_tag()
            }
        )
    )


@login_required
def dashboard(request):
    return render_to_response("probe_dispatcher/dashboard.html", RequestContext(request, {}))