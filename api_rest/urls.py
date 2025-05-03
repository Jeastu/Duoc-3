
from django.urls import path, include
from rest_framework import routers
from .views import CategoriaViewSet, ProductoViewSet, UsuarioViewSet, get_exchange_rates, search_mercadolibre, consumir_api_externa, consumir_api_externa_html


# Rutas automáticas del ViewSet
router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'productos', ProductoViewSet)
router.register(r'marcas', MarcaViewSet)
router.register(r'tipos-producto', TipoProdViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('exchange-rates/', get_exchange_rates, name='exchange-rates'),
    path('mercadolibre/search/', search_mercadolibre, name='mercadolibre-search'),
    path('externa/', consumir_api_externa, name='api_externa'),
    path('externa_html/', consumir_api_externa_html, name='api_externa_html'),
]
