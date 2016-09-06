from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
import requests

# Create your views here.

@csrf_exempt
def fiddle_editor(request):
    return render_to_response("fiddle/editor.html", RequestContext(request,request.POST))

@csrf_exempt
def get_grammar(request):
    r = requests.post(url="http://localhost:11019/image/", data=request.POST.copy());
    response = HttpResponse(r.content, content_type="application/json")
    return response