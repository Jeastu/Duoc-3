from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    TipoUsuario, Usuario, Venta, Categoria, TipoProd, Marca, Modelo,
    Producto, Region, Comuna, Direccion, Detalle
)

# Registrar modelos normales
admin.site.register(TipoUsuario)
admin.site.register(Venta)
admin.site.register(Categoria)
admin.site.register(TipoProd)
admin.site.register(Marca)
admin.site.register(Modelo)
admin.site.register(Producto)
admin.site.register(Region)
admin.site.register(Comuna)
admin.site.register(Direccion)
admin.site.register(Detalle)

# Registrar Usuario con su clase personalizada
class UsuarioAdmin(UserAdmin):
    model = Usuario
    list_display = ('username', 'email', 'nombre', 'apellido', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Información personal', {'fields': ('nombre', 'apellido', 'email', 'tipousuario')}),
        ('Permisos', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Fechas', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'nombre', 'apellido', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('username', 'email')
    ordering = ('username',)

admin.site.register(Usuario, UsuarioAdmin)
