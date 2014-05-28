# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext

from models import Probe


def probe_list(request):
    if request.user.is_authenticated():
        return render_to_response("probe_dispatcher/probes.jinja2", RequestContext(request, {'probes': Probe.objects.all()}))
    else:
        return False