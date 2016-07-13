from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response

# Create your views here.

@csrf_exempt
def fiddle_editor(request):
    return render_to_response("fiddle/editor.html");