from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    CategoriaViewSet, 
    ProductoViewSet,
    MarcaViewSet,
    TipoProdViewSet,
    consumir_api_externa, 
    consumir_api_externa_html
)

# Rutas automáticas del ViewSet
router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'productos', ProductoViewSet)
router.register(r'marcas', MarcaViewSet)
router.register(r'tipos-producto', TipoProdViewSet)

# Rutas adicionales manuales
extra_urlpatterns = [
    path('externa/', consumir_api_externa, name='api_externa'),
    path('externa_html/', consumir_api_externa_html, name='api_externa_html'),
]

# Rutas finales
urlpatterns = router.urls + extra_urlpatterns

