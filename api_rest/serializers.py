from Inicio.models import Categoria, Producto, Usuario  # importación correcta
from rest_framework import serializers

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria  # usar modelo de Inicio
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['username', 'nombre', 'apellido', 'email', 'tipousuario']  # Excluimos la contraseña por seguridad
