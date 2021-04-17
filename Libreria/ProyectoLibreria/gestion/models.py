from django.db import models

# Create your models here.
class CategoriaModel(models.Model):
    categoriaId = models.AutoField(
        primary_key = True, #sirve para indicar que sera PK
        unique = True, # sirve para indicar que no se repetira su valor en otro registro
        null = False, #No podra caeptar valores nnulos
        db_column = 'id' #nombre en la base de datos
    )
    categoriaNombre = models.CharField(
        max_length = 45, # logitud maxima de varchar
        null = False,
        db_column = 'nombre',
        verbose_name = 'nombre', # mostrar en el panel administrativo
        help_text = 'Nombre de la categoria' #ayuda para que sea visible en el panel administrativo
    )

    def __str__(self):
        #metodo magico que permite las sobre escritura de la representacion del objeto tanto en consola conmo en el panel administrativo
        # todo metodo mágico tiene _nombre_ esa nomencaltura
        # * SIMERPRE SE RETORNA UN STRING !!!
        return self.categoriaNombre

    class Meta:  #sirve para pasar metadatos o datosadicionales desde el hijo al padre
        #https://docs.djangoproject.com/en/3.2/ref/models/fields/#field-options
        db_table = 'categorias' # cambiar el nombre de la tabla en la base datos
        verbose_name = 'categoria' #visualizar el modelo en el PA
        verbose_name_plural = 'categoria' #visualizar el modelo en plural en el PA

class ProductoModel(models.Model):
    producotId = models.AutoField( #AutoField es autoincrementable, y solamente una tabla debe tener ese campo
        primary_key = True,
        unique = True,
        null = False,
        db_column = 'id'
    )
    productoNombre = models.CharField(
        db_column = 'nombre',
        help_text = 'Nombre del producto',
        max_length = 45
    )
    productoPrecio = models.DecimalField(
        max_digits = 4,
        decimal_places = 2,
        db_column = 'precio',
        help_text = 'precio del producto',
    )
    productoDescripcion = models.TextField(
        db_column = 'descripcion'
    )
    productoCantidad = models.IntegerField(
        db_column = 'cantidad',
        null = False,
    )
    # PARA HACER LAS RELACIONES:
    # Opciones para eliminar al Padre:
    # CASCADE = permite eliminar al padre y consecuentemente eliminar a los hijos
    # PROTECT = no permite eliminar al padre siempre y cuando tenga hijos pendientes (primero se elimina a los hijos y luego al padre)
    # SET_NULL = permite eliminar al padre y luego a sus hijos su col. FK la setea en NULL (se queda huerfano)
    # DO_NOTHING = no hace nada, permite eliminar al padre y deja la FK ocn su valor anterior aunque este ya no exista (genera una mala integridad de datos)
    # RESTRICT = no permite la eliminacion y lanzara un error de tipo REstrictedError, muy similar al PROTECT
    #https://docs.djangoproject.co/en/3.1/models/fields/#arguments
    categoria = models.ForeignKey(
        to = CategoriaModel,
        db_column = 'categoria_id',
        on_delete =  models.CASCADE,#que sucede cuando el padre desea ser eliminado
        related_name = 'categoriaProductos',#sirve para poder acceder a las relaciones inversas (para saber todos los productos de uancategoria), crea un atributo en el padre
        verbose_name = 'categoria',
        help_text = 'categoria del producto'
    )
    class Meta:
        db_table = 'productos'
        verbose_name = 'producto'

class CabeceraModel(models.Model):
    #* La cabId tiene que ser pk, no acepta valores nulos, es autoincrementable.
    #* La cabFecha no acepta valores nulos
    #* La cabTipo no acpeta valores nulos, su verbose_name es 'tipo de la cabecera'
    #! adicional agregar el nombre de la tabla (cabeceras) y su verbose name (cabecera)
    TIPO_VENTA = [
        ('VEN', 'VENTA'),
        ('COM', 'COMPRA'),
    ]
    cabeceraId = models.AutoField(
        primary_key = True,
        null = False,
        db_column = 'id'
    )
    cabeceraFecha = models.DateTimeField(
        null = False,
        db_column = 'fecha'
    )
    cabeceraTipo = models.CharField(
        max_length=45,
        db_column='tipo',
        null=False,
        verbose_name='tipo de la cabecera',
        choices=TIPO_VENTA,
    )
    class Meta:
        db_table = 'cabecera'
        verbose_name = 'cabecera'

class DetalleModel(models.Model):
    #! ninguna puede admitir valores nulos
    #* definir la clase Meta con los valores que crea conveniente
    detalleId = models.AutoField(
        primary_key = True,
        null = False,
        db_column = 'id',
    )
    detalleCantidad = models.IntegerField(
        db_column = 'cantidad',
        null = False,
        verbose_name='cantidad',
        help_text='cantidad del producto a comprar'
    )
    detallePrecio = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        db_column= 'precio',
        verbose_name='precio',
        help_text='precio del producto',
    )
    producto = models.ForeignKey(
        to = ProductoModel,
        on_delete = models.CASCADE,
        related_name = 'productoDEtalles',
        db_column = 'producto_id'
    )
    cabecera = models.ForeignKey(
        to = CabeceraModel,
        on_delete = models.CASCADE,
        related_name = 'cabeceraDetalle',
        db_column='cabecera_id',
        verbose_name='cabecera'
    )
    class Meta:
        db_table = 'detalle'
        verbose_name = 'detalle'