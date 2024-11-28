from django.shortcuts import render
from contact.formulario import FormContact
from django.http import HttpResponseRedirect
from django.template.loader import render_to_string
from django.core import mail
from django.conf import settings
from django.contrib import messages

# Create your views here.
def contato(request):
    if request.method == 'POST':
        post = FormContact(request.POST)
        if post.is_valid() == True:
            email = render_to_string('contact/contact_email.txt', post.cleaned_data)
            mail.send_mail(
                "Mensagem enviada", 
                email, 
                post.cleaned_data["email"], 
                [post.cleaned_data["email"], settings.DEFAULT_FROM_EMAIL]
                )
            messages. success(request, 'Contato enviado com sucesso!')
            return HttpResponseRedirect('/contact/')
        else:
            return render(request, 'contact/contact_form.html', {'form': post})
    else:
        return render(request, 'contact/contact_form.html', {'form': FormContact()})