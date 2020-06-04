# Generated by Django 3.0.3 on 2020-04-07 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('especialista', '0014_especialista_paci'),
        ('especialista_paciente', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='especialistapaciente',
            old_name='pac',
            new_name='paciente',
        ),
        migrations.AlterField(
            model_name='especialistapaciente',
            name='specialist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='atende', to='especialista.Especialista'),
        ),
    ]
