# Generated by Django 3.0.3 on 2020-03-24 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('especialista', '0003_auto_20200324_1953'),
    ]

    operations = [
        migrations.AddField(
            model_name='especialista',
            name='teste',
            field=models.BigIntegerField(default=0),
        ),
    ]