from django.urls import path, include
from rest_framework import routers
from .views import CategoriaViewSet, ProductoViewSet, UsuarioViewSet, get_exchange_rates, search_mercadolibre, consumir_api_externa, consumir_api_externa_html

router = routers.DefaultRouter()
router.register('categoria', CategoriaViewSet)
router.register('productos', ProductoViewSet)
router.register('usuarios', UsuarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('exchange-rates/', get_exchange_rates, name='exchange-rates'),
    path('mercadolibre/search/', search_mercadolibre, name='mercadolibre-search'),
    path('externa/', consumir_api_externa, name='api_externa'),
    path('externa_html/', consumir_api_externa_html, name='api_externa_html'),
]
