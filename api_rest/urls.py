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
from .serializers import CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Clase personalizada para emitir el token
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

# ViewSets (endpoints automáticos)
router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'productos', ProductoViewSet)
router.register(r'marcas', MarcaViewSet)
router.register(r'tipos-producto', TipoProdViewSet)

# Rutas finales
urlpatterns = router.urls + [
    path('externa/', consumir_api_externa, name='api_externa'),
    path('externa_html/', consumir_api_externa_html, name='api_externa_html'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
