# Generated by Django 2.2.14 on 2022-11-18 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prueba', '0002_prueba_nombre_prueba'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prueba',
            name='nombre_prueba',
        ),
    ]
