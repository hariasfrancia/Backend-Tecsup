from rest_framework import serializers
from .models import CategoriaModel

# Hay dos tipos de serializadores
# 1. un serializador enel cual no es necesario usar un modelo (crear una plantilla comun para capturar datos que no necesariamente corresponderan a un model)
# 2. un serializador basado en un modelo (tabla) jalara todosl os campos definidos como parte del serializador

class MostrarCategoriasSerializer(serializers.ModelSerializer):
    class Meta:
        # Estos atributos son obligatorios en el caso que usemos un ModelSerializaer
        model = CategoriaModel # con esto se vinculo el serializador con el modelo
        # que campos queremos utilizar de ese modelo para el serializador
        # recibe 3 valores: '__all__' | ['categoriaNombre'] | ['categoriaNombre', 'categoriaOtro']
        fields =  '__all__'
        # o bien podriamos usar el atributo exluce = []
        # exclude = ['categoriaId','categoriaOtro', '...']
        # ? NOTA: NO PODEMOS USAR fields Y exclude al mismo tiempo, OBLIGATORIAMENTE TENEMOS QUE USAR UNO DE LOS DOS
