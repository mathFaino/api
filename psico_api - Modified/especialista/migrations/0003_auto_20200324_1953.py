# Generated by Django 3.0.3 on 2020-03-24 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('especialista', '0002_auto_20200324_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='especialista',
            name='CRM',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='especialista',
            name='CRP',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
    ]