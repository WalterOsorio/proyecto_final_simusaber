# Generated by Django 2.2.14 on 2022-11-18 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bancoPregunta', '0003_retroalimentacion_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='bancopregunta',
            name='nombre',
            field=models.CharField(max_length=225, null=True),
        ),
    ]
