# Generated by Django 3.0.3 on 2020-06-04 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('especialista', '0014_especialista_paci'),
    ]

    operations = [
        migrations.AddField(
            model_name='especialista',
            name='imagem_perfil',
            field=models.ImageField(blank=True, null=True, upload_to='imagens'),
        ),
    ]
