# Generated by Django 5.1.1 on 2024-10-05 18:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0005_remove_equipo_marcacontrolador_and_more'),
        ('energiaplantas', '0005_equipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipo',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clientes.cliente'),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='marcacontrolador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='energiaplantas.marcacontrolador'),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='marcagenerador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='energiaplantas.marcagenerador'),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='marcamodulo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='energiaplantas.marcamodulo'),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='marcamotor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='energiaplantas.marcamotor'),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='uso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='energiaplantas.uso'),
        ),
    ]
