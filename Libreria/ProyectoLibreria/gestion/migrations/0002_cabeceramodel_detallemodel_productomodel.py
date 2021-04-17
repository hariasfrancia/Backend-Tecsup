# Generated by Django 3.2 on 2021-04-17 01:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0001_initial_migration'),
    ]

    operations = [
        migrations.CreateModel(
            name='CabeceraModel',
            fields=[
                ('cabeceraId', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('cabeceraFecha', models.DateTimeField(db_column='fecha')),
                ('cabeceraTipo', models.CharField(choices=[('VEN', 'VENTA'), ('COM', 'COMPRA')], db_column='tipo', max_length=45, verbose_name='tipo de la cabecera')),
            ],
            options={
                'verbose_name': 'cabecera',
                'db_table': 'cabecera',
            },
        ),
        migrations.CreateModel(
            name='ProductoModel',
            fields=[
                ('producotId', models.AutoField(db_column='id', primary_key=True, serialize=False, unique=True)),
                ('productoNombre', models.CharField(db_column='nombre', help_text='Nombre del producto', max_length=45)),
                ('productoPrecio', models.DecimalField(db_column='precio', decimal_places=2, help_text='precio del producto', max_digits=4)),
                ('productoDescripcion', models.TextField(db_column='descripcion')),
                ('productoCantidad', models.IntegerField(db_column='cantidad')),
                ('categoria', models.ForeignKey(db_column='categoria_id', help_text='categoria del producto', on_delete=django.db.models.deletion.CASCADE, related_name='categoriaProductos', to='gestion.categoriamodel', verbose_name='categoria')),
            ],
            options={
                'verbose_name': 'producto',
                'db_table': 'productos',
            },
        ),
        migrations.CreateModel(
            name='DetalleModel',
            fields=[
                ('detalleId', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('detalleCantidad', models.IntegerField(db_column='cantidad', help_text='cantidad del producto a comprar', verbose_name='cantidad')),
                ('detallePrecio', models.DecimalField(db_column='precio', decimal_places=2, help_text='precio del producto', max_digits=4, verbose_name='precio')),
                ('cabecera', models.ForeignKey(db_column='cabecera_id', on_delete=django.db.models.deletion.CASCADE, related_name='cabeceraDetalle', to='gestion.cabeceramodel', verbose_name='cabecera')),
                ('producto', models.ForeignKey(db_column='producto_id', on_delete=django.db.models.deletion.CASCADE, related_name='productoDEtalles', to='gestion.productomodel')),
            ],
            options={
                'verbose_name': 'detalle',
                'db_table': 'detalle',
            },
        ),
    ]
