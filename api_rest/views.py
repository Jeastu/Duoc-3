from django.shortcuts import render

# Create your views here.
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

class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class TipoProdViewSet(viewsets.ModelViewSet):
    queryset = TipoProd.objects.all()
    serializer_class = TipoProdSerializer


import requests
from django.http import JsonResponse

def consumir_api_externa(request):
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)

    # Retorna como JSON nativo
    return JsonResponse(response.json(), safe=False)



import requests
from django.shortcuts import render

def consumir_api_externa_html(request):
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    datos = response.json()
    return render(request, 'api_rest/externa.html', {'posts': datos})

