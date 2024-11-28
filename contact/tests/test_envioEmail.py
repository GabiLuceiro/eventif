from django.test import TestCase
from django.core import mail

class email(TestCase):
    def setUp(self):
        data = dict(
            name = "Gabi",
            phone = "53912345678",
            email = "gabriela.luceiro@aluno.riogrande.ifrs.edu.br",
            message = "mensagem"
        )
        self.client.post('/contact/', data)
        self.envio = mail.outbox[0]

    def test_componentes(self):
        componentes = [
            ["Mensagem enviada", self.envio.subject],
            ["gabriela.luceiro@aluno.riogrande.ifrs.edu.br", self.envio.from_email],
            [["gabriela.luceiro@aluno.riogrande.ifrs.edu.br", "contato@eventif.com.br"], self.envio.to]
        ]
        for item in componentes:
            with self.subTest():
                self.assertEqual(item[0], item[1])

    def test_dados(self):
        dados = [
            "Gabi",
            "53912345678",
            "gabriela.luceiro@aluno.riogrande.ifrs.edu.br",
            "mensagem"
        ]
        for item in dados:
            with self.subTest():
                self.assertIn(item, self.envio.body)