from django.shortcuts import render, render_to_response

# Create your views here.
from django.template import RequestContext

def home(request):
	return render_to_response('index.html', context_instance=RequestContext(request))# Create your views here.