from Inicio.models import Categoria  # ✅ importación correcta
from rest_framework import serializers

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria  # ✅ usar modelo de Inicio
        fields = '__all__'

