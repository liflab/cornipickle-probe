# -*- coding: utf-8 -*-
import json
import ast
from django.http import HttpResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404,redirect
from probe_project.apps.probe_dispatcher.models import Probe
from probe_project.apps.dashboard.models import Datum
from django.shortcuts import render_to_response
from django.utils.translation import ugettext_lazy as _
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from probe_project.apps.dashboard.signals import cornipickle_verdict_false

from django.http.response import Http404, JsonResponse
import requests

@csrf_exempt
def image(request):
    postDict = request.POST.copy()
    if "interpreter" in postDict:
        r = requests.post(url="http://localhost:11019/image/", data=postDict)
        if r.status_code == 200:
            response = HttpResponse(r.content, content_type="application/json")
            # signal ici
            current_data = response.content
            current_data = ast.literal_eval(current_data)
            data = json.dumps(current_data)
            data = json.loads(data)
            if data['global-verdict'] != True:
                cornipickle_verdict_false.send(sender=image,response=request.META,probe= postDict["id"],user=1)
            #if response['verdirt'] == false
            # cornipickle_verdict_false.send(probe = postDict['Probe],response= postDict,user = request.user)
            return response
    else:
        probeId = postDict["id"]
        current_probe = get_object_or_404(Probe, pk=probeId)
        if current_probe.hash != postDict["hash"] or current_probe.tags_attributes_interpreter["interpreter"] == '':
            messages.error(request,_("Vérifier si l'interpréteur Cornipickle fonctionne sur votre site. Il ce peut"
                                     "qui vous ayez fait des modifications à votre sonde sans changer le script sur votre"
                                     "page web."))
            raise Http404(messages)
        postDict["interpreter"] = current_probe.tags_attributes_interpreter["interpreter"]
        r = requests.post(url="http://localhost:11019/image/", data=postDict)
        response = HttpResponse(r.content, content_type="application/json")
        # Signal ici
        return response


@login_required
def datum(request):
    if request.user.is_authenticated():
        list_datum = Datum.objects.filter(user_id=request.user.id)
        if len(list_datum) == 0:
            list_datum = None
        return render_to_response("dashboard/datums.html", RequestContext(request, {
            'datums': list_datum
        }))
    else:
        return redirect('/')