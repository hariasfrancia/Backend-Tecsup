# Generated by Django 3.2 on 2021-04-17 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0002_cabeceramodel_detallemodel_productomodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productomodel',
            old_name='producotId',
            new_name='productoId',
        ),
        migrations.AlterField(
            model_name='productomodel',
            name='productoNombre',
            field=models.CharField(db_column='nombre', help_text='Nombre del producto', max_length=45, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='productomodel',
            name='productoPrecio',
            field=models.DecimalField(db_column='precio', decimal_places=2, help_text='precio del producto', max_digits=4, verbose_name='precio del producto'),
        ),
    ]