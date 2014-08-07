from django.shortcuts import render_to_response, render
from django.template import RequestContext

from forms import ContactForms
from django.core.mail import EmailMultiAlternatives #para enviar html
from django.core.mail import EmailMessage

def mensajes(request):
	info_enviado = False
	email = ""
	titulo = ""
	texto = ""
	if request.method == "POST":
		formulario = ContactForms(request.POST)
		if formulario.is_valid():
			info_enviado = True
			email = formulario.cleaned_data['Email']
			titulo = formulario.cleaned_data['Titulo']
			texto = formulario.cleaned_data['Texto']

			#configuracion para el envio al email
			to_admin = 'proyecto.sia.py@gmail.com'
			html_content = "Informacion recibida de [%s] <br><br>Titulo: %s<br><br>Mensaje: <p>%s</p>"%(email,titulo,texto)
			mge = EmailMultiAlternatives('correo de contacto',html_content,'from@server.com',[to_admin])
			mge.attach_alternative(html_content,'text/html') #aqui se degine el contenido como html
			mge.send() #envia en mje
	else:
		formulario = ContactForms()
	ctx = {'form':formulario, 'info_enviado':info_enviado}
	return render_to_response('mje.html', ctx, context_instance=RequestContext(request))

