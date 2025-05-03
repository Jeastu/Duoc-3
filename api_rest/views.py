from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CategoriaSerializer, ProductoSerializer, UsuarioSerializer
from Inicio.models import Categoria, Producto, Usuario
import requests

# Create your views here.
 api-changes

from rest_framework import viewsets
from Inicio.models import Categoria, Producto, Marca, TipoProd
from .serializers import (
    CategoriaSerializer, 
    ProductoSerializer,
    MarcaSerializer,
    TipoProdSerializer
)


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

@api_view(['GET'])
def get_exchange_rates(request):
    """
    Get exchange rates from exchangerate.host
    """
    try:
        base_currency = request.GET.get('base', 'CLP')
        symbols = request.GET.get('symbols', 'USD,EUR')
        
        response = requests.get(f'https://api.exchangerate.host/latest?base={base_currency}&symbols={symbols}')
        if response.status_code == 200:
            return Response(response.json())
        return Response({'error': 'Error getting exchange rates'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def search_mercadolibre(request):
    """
    Search products in MercadoLibre
    """
    try:
        query = request.GET.get('q', '')
        if not query:
            return Response({'error': 'Query parameter is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        response = requests.get(f'https://api.mercadolibre.com/sites/MLC/search?q={query}')
        if response.status_code == 200:
            return Response(response.json())
        return Response({'error': 'Error searching in MercadoLibre'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




def consumir_api_externa(request):
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)

    # Retorna como JSON nativo
    return JsonResponse(response.json(), safe=False)



def consumir_api_externa_html(request):
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    datos = response.json()
    return render(request, 'api_rest/externa.html', {'posts': datos})
