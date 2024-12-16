from django.db import models

class ContactModel(models.Model):
    name = models.CharField('NOME', max_length=50)
    phone = models.CharField('N° DE TELEFONE', max_length=20, blank=True)
    email = models.EmailField('EMAIL')
    message = models.TextField('MENSAGEM', max_length=200)
    created_at = models.DateTimeField('CRIADO EM', auto_now_add=True)
    response = models.TextField('RESPOSTA', max_length=200)
    r_created_at = models.DateTimeField('RESPOSTA CRIADA EM', null=True, blank=True)
    flag = models.BooleanField('RESPONDIDO', default=False)

    class Meta:
        verbose_name = 'contato'
        verbose_name_plural = 'contatos'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name