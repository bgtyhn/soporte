from django.http import HttpResponse
from django.template import loader, RequestContext
from django.shortcuts import render_to_response
from .models import Token

def index(request):
	template = loader.get_template('redes/index.html')
	context = {}
	token = request.GET['token']
	print(token)
	redirect = Token.objects.get(token = token);
	print(redirect)
	context['redirect'] = redirect
	return HttpResponse(template.render(context, request))

def handler404(request):
    response = render_to_response('redes/404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response

# Create your views here.