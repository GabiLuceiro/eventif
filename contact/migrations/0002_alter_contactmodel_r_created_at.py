# Generated by Django 5.1 on 2024-12-15 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmodel',
            name='r_created_at',
            field=models.DateTimeField(null=True, verbose_name='RESPOSTA CRIADA EM'),
        ),
    ]
