# Generated by Django 3.0.3 on 2020-03-24 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('especialista', '0004_especialista_teste'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='especialista',
            name='teste',
        ),
        migrations.AlterField(
            model_name='especialista',
            name='telefone',
            field=models.BigIntegerField(max_length=11),
        ),
    ]