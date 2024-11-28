from django.test import TestCase
from contact.formulario import FormContact

class form(TestCase):
    def setUp(self):
        self.form = FormContact()

    def test_FORMULARIO(self):
        campos = ['name', 'phone', 'email', 'message']
        self.assertSequenceEqual(campos, list(self.form.fields))