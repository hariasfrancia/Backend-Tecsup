from rest_framework.generics import ListAPIView, RetrieveDestroyAPIView, ListCreateAPIView
from rest_framework.response import Response
from .models import CategoriaModel
from .serializers import MostrarCategoriasSerializer

#creamos una clase
class ListarCategoriaController(ListCreateAPIView):
    # El atributo queryset es el encargado de hacer la consulta a la base de datos para rellenar la respuesta en la vista generica
    # SELECT * FROM CATEGORIAS (sentencia SQL) (sentencias RAW)
    queryset = CategoriaModel.objects.all()
    serializer_class = MostrarCategoriasSerializer

# Tercer paso, crear la ruta
# C => Create
# R => Read
# U => Update
# D  =>Delete
class CRUDCategoriaController(RetrieveDestroyAPIView):
    queryset = CategoriaModel.objects.all()
    serializer_class = MostrarCategoriasSerializer
