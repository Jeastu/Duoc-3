
from Inicio.models import Categoria, Producto, Usuario  # importación correcta
from Inicio.models import Marca, TipoProd

from rest_framework import serializers

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria  # usar modelo de Inicio
        fields = '__all__'
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = '__all__'

class TipoProdSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoProd
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['username', 'nombre', 'apellido', 'email', 'tipousuario']  # Excluimos la contraseña por seguridad
