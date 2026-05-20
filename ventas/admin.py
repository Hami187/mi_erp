from django.contrib import admin
from .models import Venta, DetalleVenta


class DetalleVentaInline(admin.TabularInline):
    model = DetalleVenta
    extra = 1
    readonly_fields = ['subtotal']


@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ['numero', 'cliente', 'fecha', 'estado', 'total']
    search_fields = ['numero', 'cliente__nombre']
    list_filter = ['estado']
    readonly_fields = ['total']
    inlines = [DetalleVentaInline]