# Generated by Django 3.0.3 on 2020-04-13 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0004_paciente_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='CPF',
            field=models.BigIntegerField(),
        ),
    ]