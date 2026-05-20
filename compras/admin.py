from django.contrib import admin
from .models import Compra, DetalleCompra


class DetalleCompraInline(admin.TabularInline):
    model = DetalleCompra
    extra = 1
    readonly_fields = ['subtotal']


@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ['numero', 'proveedor', 'fecha', 'estado', 'total']
    search_fields = ['numero', 'proveedor__nombre']
    list_filter = ['estado']
    readonly_fields = ['total']
    inlines = [DetalleCompraInline]