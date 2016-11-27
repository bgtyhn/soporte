from django.http import HttpResponse
from django.template import loader
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

# Create your views here.