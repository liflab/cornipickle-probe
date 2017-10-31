from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
import requests
import json

# Create your views here.

@csrf_exempt
def fiddle_editor(request):
    return render_to_response("fiddle/editor.html", RequestContext(request,request.POST))

@csrf_exempt
def get_grammar(request):
    data = json.dumps(request.POST.copy())
    r = requests.post(url="http://localhost:11019/fiddle/", data=data)
    response = HttpResponse(r.content, content_type="application/json")
    return response

@csrf_exempt
def fiddle_js(request):
    return render_to_response("fiddle/fiddle.js", RequestContext(request))