from django.test import TestCase
from django.core import mail
from contact.formulario import FormContact
from contact.models import ContactModel

class postValido(TestCase):
    def setUp(self):
        data = dict(
            name = "Gabi",
            phone = "53912345678",
            email = "gabriela.luceiro@aluno.riogrande.ifrs.edu.br",
            message = "mensagem"
        )
        self.res = self.client.post('/contact/', data)

    def test_email(self):
        self.assertEqual(1, len(mail.outbox))

    def test_statusCode(self):
        self.assertEqual(302, self.res.status_code)

    def test_salvar(self):
        self.assertTrue(ContactModel.objects.exists())

class postInvalido(TestCase):
    def setUp(self):
        self.res = self.client.post('/contact/', {})

    def test_statusCode(self):
        self.assertEqual(200, self.res.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.res, 'contact/contact_form.html')

    def test_formulario(self):
        formulario = self.res.context['form']
        self.assertIsInstance(formulario, FormContact)

    def test_erros(self):
        formulario = self.res.context['form']
        self.assertTrue(formulario.errors)
    
    def test_naoSalvar(self):
        self.assertFalse(ContactModel.objects.exists())

class emailResposta(TestCase):
    def setUp(self):
        self.obj = ContactModel.objects.create(
            name = "Gabi",
            phone = "53912345678",
            email = "gabriela.luceiro@aluno.riogrande.ifrs.edu.br",
            message = "mensagem"
        )

    def test_emailNaoEnvia(self):
        self.assertEqual(0, len(mail.outbox))

    def test_emailEnvia(self):
        self.obj.response = "resposta"
        self.obj.save()
        self.assertEqual(1, len(mail.outbox))