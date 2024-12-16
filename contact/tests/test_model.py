from django.test import TestCase
from contact.models import ContactModel
from datetime import datetime

class modelContact(TestCase):
    def setUp(self):
        self.obj = ContactModel.objects.create(
            name = "Gabi",
            phone = "53912345678",
            email = "gabriela.luceiro@aluno.riogrande.ifrs.edu.br",
            message = "mensagem"
        )

    def test_existe(self):
        self.assertTrue(ContactModel.objects.exists())

    def test_created_at(self):
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Gabi', str(self.obj))

    def test_flagFalse(self):
        self.assertEqual(False, self.obj.flag)
    
    def test_telefoneBlank(self):
        self.assertTrue(ContactModel._meta.get_field('phone').blank)

    def test_respostaNull(self):
        self.assertTrue(ContactModel._meta.get_field('r_created_at').null)

    def test_respostaBlank(self):
        self.assertTrue(ContactModel._meta.get_field('r_created_at').blank)