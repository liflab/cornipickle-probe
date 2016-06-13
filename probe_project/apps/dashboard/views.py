# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from probe_project.apps.probe_dispatcher.models import Probe, Sensor
from django.http import Http404
from django.utils.translation import ugettext_lazy as _
import requests


@csrf_exempt
def image(request):
    postDict = request.POST.copy()
    if "interpreter" in postDict:
        r = requests.post(url="http://localhost:11019/image/", data=postDict)
        response = HttpResponse(r.content, content_type="application/json")
        return response
    else:
        current_probe = get_object_or_404(Probe, pk=postDict["id"])
        if current_probe.hash != postDict["hash"] or current_probe.tags_attributes_interpreter["interpreter"] == '':
            messages.error(request,_("Vérifier si l'interpréteur Cornipickle fonctionne sur votre site. Il ce peut"
                                     "qui vous ayez fait des modifications à votre sonde sans changer le script sur votre"
                                     "page web."))
            raise Http404(messages)
        postDict["interpreter"] = current_probe.tags_attributes_interpreter["interpreter"]
        r = requests.post(url="http://localhost:11019/image/", data=postDict)
        response = HttpResponse(r.content, content_type="application/json")
        return response



