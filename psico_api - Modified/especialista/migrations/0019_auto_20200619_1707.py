# Generated by Django 3.0.3 on 2020-06-19 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('especialista', '0018_remove_especialista_imagem_perfil'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='especialista',
            name='teste',
        ),
        migrations.AddField(
            model_name='especialista',
            name='imagem_perfil',
            field=models.FileField(blank=True, null=True, upload_to='imagens'),
        ),
    ]
