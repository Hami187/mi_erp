from django.contrib import admin
from .models import Categoria, Producto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion']
    search_fields = ['nombre']


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nombre', 'categoria', 'proveedor', 'precio_compra', 'precio_venta', 'stock', 'activo']
    search_fields = ['codigo', 'nombre']
    list_filter = ['categoria', 'activo']