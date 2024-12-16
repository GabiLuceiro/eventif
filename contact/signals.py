from django.dispatch import receiver
from django.db.models.signals import pre_save
from contact.models import ContactModel
from django.core import mail
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.timezone import now

@receiver(pre_save, sender=ContactModel)
def emailResposta(sender, instance, **kwargs):
    if instance.flag == False and instance.response != '':
        contexto = {'nome': instance.name, 
                    'phone': instance.phone,
                    'email': instance.email,
                    'message': instance.message,
                    'response': instance.response
                    }
        email = render_to_string('contact/contact_response.txt', contexto)
        mail.send_mail(
            "Mensagem enviada", 
            email, 
            settings.DEFAULT_FROM_EMAIL, 
            [instance.email, settings.DEFAULT_FROM_EMAIL]
            )
        instance.flag = True
        instance.r_created_at = now()