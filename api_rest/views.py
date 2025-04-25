from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from Inicio.models import Categoria
from .serializers import CategoriaSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


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

