from django import forms
class FormContact(forms.Form):
    name = forms.CharField(label='Nome')
    phone = forms.CharField(label='Telefone', required=False)
    email = forms.EmailField(label='Email')
    message = forms.CharField(label='Mensagem', widget=forms.Textarea)