# Generated by Django 3.0.3 on 2020-04-13 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0005_auto_20200413_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='CPF',
            field=models.CharField(max_length=11),
        ),
    ]
