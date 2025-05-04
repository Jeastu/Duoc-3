from Inicio.models import Categoria, Producto, Marca, TipoProd  # importación correcta
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        # Crear el token manualmente
        token = RefreshToken()

        # Asigna el user_id como username, ya que no tienes 'id'
        token['user_id'] = user.username
        token['username'] = user.username
        token['email'] = user.email
        token['tipo'] = user.tipousuario.nombreTipo

        # Retorna el token que tú creaste (no el de super().get_token)
        return token


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria  # ✅ usar modelo de Inicio
        fields = '__all__'
        depth = 1
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'
        depth = 1

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = '__all__'
        depth = 1

class TipoProdSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoProd
        fields = '__all__'
        depth = 1



