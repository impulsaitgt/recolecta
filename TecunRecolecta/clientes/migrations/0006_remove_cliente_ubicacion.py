# Generated by Django 5.1.1 on 2024-10-05 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0005_remove_equipo_marcacontrolador_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='ubicacion',
        ),
    ]
