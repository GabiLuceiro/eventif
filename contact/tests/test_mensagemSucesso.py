from django.test import TestCase

class mensagemSucesso(TestCase):
    def test_sucesso(self):
        data = dict(
            name = "Gabi",
            phone = "53912345678",
            email = "gabriela.luceiro@aluno.riogrande.ifrs.edu.br",
            message = "mensagem"
        )
        res = self.client.post('/contact/', data, follow=True)
        self.assertContains(res, "Contato enviado com sucesso!")