# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from probe_project.apps.probe_dispatcher.forms import ProbeFrontendForm, SensorFrontendForm
from probe_project.apps.probe_dispatcher.models import Probe, Sensor, User
import json
from datetime import datetime


@login_required
def probe_detail(request, probe_id):
    current_probe = get_object_or_404(Probe, pk=probe_id)
    if current_probe.user_id == request.user.id or request.user.is_staff:
        return render_to_response("probe_dispatcher/probe_detail.html", RequestContext(request, {
            'probe': current_probe
        }))
    else:
        return redirect('/')


# http://stackoverflow.com/questions/1854237/django-edit-form-based-on-add-form
@login_required
def probe_form(request, probe_id=None):
    if probe_id:
        probe = get_object_or_404(Probe,pk=probe_id)
        if probe.user != request.user:
            return HttpResponseForbidden()
    else:
        probe = None

    if request.method == 'POST':
        form = ProbeFrontendForm(request.POST, instance=probe)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            form.save_m2m()
            return HttpResponseRedirect(reverse(probe_detail, args=(instance.id,)))
        else:
            return render_to_response("probe_dispatcher/probe_form.html", RequestContext(request, {'form': form,}))
    else:
        form = ProbeFrontendForm(instance=probe)
    return render_to_response("probe_dispatcher/probe_form.html", RequestContext(request, {'form': form, }))


@login_required
def probe_delete(request, probe_id):
    probe = get_object_or_404(Probe, pk=probe_id)
    if probe.user != request.user:
        return HttpResponseForbidden()
    probe.delete()
    return render_to_response("probe_dispatcher/probes.html", RequestContext(request, {
        'probes': Probe.objects.filter(user=request.user)
        }))


@login_required
def probe_add_corni(request, probe_id):
    probe = get_object_or_404(Probe, pk=probe_id)
    if probe.is_enabled:
        probe.add_property()
    return render_to_response("probe_dispatcher/probes.html", RequestContext(request, {
        'probes': Probe.objects.filter(user=request.user)
        }))


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
    return render_to_response("probe_dispatcher/sensors.html", RequestContext(request, {
        'sensors': Sensor.objects.filter(user__in=[request.user, User.objects.get(username="admin")])
    }))


# http://stackoverflow.com/questions/1854237/django-edit-form-based-on-add-form
@login_required
def sensor_form(request, sensor_id=None):
    if sensor_id:
        sensor = get_object_or_404(Sensor, pk=sensor_id)
        if sensor.user != request.user:
            return HttpResponseForbidden()
    else:
        sensor = None

    if request.method == 'POST':
        form = SensorFrontendForm(request.POST, instance=sensor)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return HttpResponseRedirect(reverse(sensor_detail, args=(instance.id,)))
        else:
            return render_to_response("probe_dispatcher/sensor_form.html", RequestContext(request, {'form': form, }))
    else:
        form = SensorFrontendForm(instance=sensor)
    return render_to_response("probe_dispatcher/sensor_form.html", RequestContext(request, {'form': form, }))


@login_required
def sensor_detail(request, sensor_id):
    current_sensor = get_object_or_404(Sensor, pk=sensor_id)
    if current_sensor.user_id == request.user.id or request.user.is_staff:
        return render_to_response("probe_dispatcher/sensor_detail.html", RequestContext(request, {
            'sensor': current_sensor
        }))
    else:
        return redirect('/')


@login_required
def sensor_delete(request, sensor_id):
    sensor = get_object_or_404(Sensor, pk=sensor_id)
    if sensor.user != request.user:
        return HttpResponseForbidden()
    sensor.delete()
    return render_to_response("probe_dispatcher/sensors.html", RequestContext(request, {
        'sensors': Sensor.objects.filter(user__in=[request.user, User.objects.get(username="admin")])
        }))


def probe_file(request, probe_id, probe_hash, banner=True):
    current_probe = get_object_or_404(Probe, id=probe_id)
    if current_probe.hash != probe_hash:
        raise Http404

    for sensor in current_probe.sensors.all():
        print(sensor.name)

    encoded_tagnames = json.dumps(current_probe.tags_and_attributes["tagnames"])
    encoded_attributes = json.dumps(current_probe.tags_and_attributes["attributes"])

    return render_to_response(
        "probe_dispatcher/probe.inc.js",
        RequestContext(
            request, {
                'id': probe_id,
                'hash': probe_hash,
                'banner': banner,
                'server_name': 'localhost:' + str(11000 + int(probe_id)),
                'tags': encoded_tagnames,
                'attributes': encoded_attributes,
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
        "probe_dispatcher/test2.html",
        RequestContext(
            request, {
                'script': current_probe.get_script_tag()
            }
        )
    )


@login_required
def dashboard(request):
    return render_to_response("probe_dispatcher/dashboard.html", RequestContext(request, {}))