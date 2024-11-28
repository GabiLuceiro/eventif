from django.test import TestCase

class get(TestCase):
    def setUp(self):
        self.res = self.client.get('/contact/')

    def test_template(self):
        self.assertTemplateUsed(self.res, 'contact/contact_form.html')

    def test_middleware(self):
        self.assertContains(self.res, 'csrfmiddlewaretoken')

    def test_formulario(self):
        campos = (
            ('<form', 1),
            ('<input', 5),
            ('type="text"', 2),
            ('type="email"', 1),
            ('type="submit"', 1),
            ('<textarea', 1)
        )
        for item, numero in campos:
            with self.subTest():
                self.assertContains(self.res, item, numero)

    def test_statusCode(self):
        self.assertEqual(200, self.res.status_code)