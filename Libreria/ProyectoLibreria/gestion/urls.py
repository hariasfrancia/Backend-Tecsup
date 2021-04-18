from django.urls import path
from .views import ListarCategoriaController

# !Esta variable se tiene quellamar SI o SI así:
urlpatterns = [
    path('categorias', ListarCategoriaController.as_view()),
]
