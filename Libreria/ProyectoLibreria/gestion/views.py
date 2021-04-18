from .models import CategoriaModel
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

#creamos una clase
class ListarCategoriaController(ListAPIView):
    # El atributo queryset es el encargado de hacer la consulta a la base de datos para rellenar la respuesta en la vista generica
    # SELECT * FROM CATEGORIAS (sentencia SQL) (sentencias RAW)
    queryset = CategoriaModel.objects.all()

# Tercer paso, crear la ruta
