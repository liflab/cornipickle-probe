# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext

from models import Probe, Sensor


def probes(request):
    if request.user.is_authenticated():
        return render_to_response("probe_dispatcher/probes.jinja2", RequestContext(request, {
            'probes': Probe.objects.all()
        }))
    else:
        return False

def probe_file(request, id, hash):
    return render_to_response("probe_dispatcher/probe.jinja2", RequestContext(request, {'id' : id, 'hash' : hash}), content_type='application/javascript')


def dashboard(request):
    return render_to_response("probe_dispatcher/dashboard.jinja2", RequestContext(request, {}))