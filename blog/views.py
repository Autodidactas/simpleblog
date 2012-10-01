# Create your views here.
from models import *
from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
	lista_post = Posts.objects.all().order_by('-id')[:3]
	return render_to_response('index.html', locals(),
		  context_instance=RequestContext(request))
