# Generated by Django 3.0.3 on 2020-06-08 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analise_video', '0004_remove_analisevideo_relatorio'),
    ]

    operations = [
        migrations.AddField(
            model_name='analisevideo',
            name='video',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]