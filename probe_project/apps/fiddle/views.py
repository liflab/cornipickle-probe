from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.

@csrf_exempt
def fiddle_editor(request):
    return render_to_response("fiddle/editor.html", RequestContext(request,request.POST));