from django.shortcuts import render

from contact.formulario import FormContact

# Create your views here.
def contato(request):
    return render(request, 'contact/contact_form.html', {'form': FormContact()})