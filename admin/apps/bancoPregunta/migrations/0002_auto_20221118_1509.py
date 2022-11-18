# Generated by Django 2.2.14 on 2022-11-18 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bancoPregunta', '0001_initial'),
        ('states', '0001_initial'),
        ('prueba', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pruebabancopregunta',
            name='prueba',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='prueba.Prueba'),
        ),
        migrations.AddField(
            model_name='bancopregunta',
            name='estado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='states.Estado'),
        ),
        migrations.AddField(
            model_name='bancopregunta',
            name='grado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='prueba.Grado'),
        ),
        migrations.AddField(
            model_name='bancopregunta',
            name='materia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='prueba.Materia'),
        ),
    ]
