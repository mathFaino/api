# Generated by Django 3.0.3 on 2020-06-03 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analise_video', '0003_auto_20200428_1548'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='analisevideo',
            name='relatorio',
        ),
    ]
