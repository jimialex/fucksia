from django.shortcuts import render, render_to_response ,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as social_logout

from .models import Estudiante
from .forms import EstudianteForm

def login(request):
	if not request.user.is_authenticated():
		return render_to_response('login.html', context_instance=RequestContext(request))
	else:
		return redirect('home')

@login_required
def logout(request):
	social_logout(request)
	return redirect('login')

@login_required
def perfil(request):
	estudiante = Estudiante.objects.get(uid=request.user)
	if request.method == 'POST':
		form = EstudianteForm(request.POST, instance=estudiante)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = EstudianteForm(instance=estudiante)

	return render_to_response('perfil.html', context_instance=RequestContext(request, locals()))
