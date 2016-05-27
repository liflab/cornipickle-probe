from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from probe_project.apps.probe_dispatcher.models import Probe
from django.http import Http404
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
            raise Http404
        postDict["interpreter"] = current_probe.tags_attributes_interpreter["interpreter"]
        r = requests.post(url="http://localhost:11019/image/", data=postDict)
        response = HttpResponse(r.content, content_type="application/json")
        return response
