from django.urls import path
from .views import ListarCategoriaController, CRUDCategoriaController

# !Esta variable se tiene quellamar SI o SI así:
urlpatterns = [
    path('categorias', ListarCategoriaController.as_view()),
    path('categorias/<int:pk>', CRUDCategoriaController.as_view()),
]
