# Generated by Django 3.0.3 on 2020-04-04 23:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('especialista', '0012_auto_20200404_1932'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='especialista',
            name='pacS',
        ),
        migrations.DeleteModel(
            name='EspecialistaPaciente',
        ),
    ]
