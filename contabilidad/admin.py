from django.contrib import admin
from .models import CuentaPorCobrar, CuentaPorPagar


@admin.register(CuentaPorCobrar)
class CuentaPorCobrarAdmin(admin.ModelAdmin):
    list_display = ['numero', 'cliente', 'monto', 'monto_pagado', 'saldo', 'fecha_vencimiento', 'estado']
    search_fields = ['numero', 'cliente__nombre']
    list_filter = ['estado']
    readonly_fields = ['saldo']


@admin.register(CuentaPorPagar)
class CuentaPorPagarAdmin(admin.ModelAdmin):
    list_display = ['numero', 'proveedor', 'monto', 'monto_pagado', 'saldo', 'fecha_vencimiento', 'estado']
    search_fields = ['numero', 'proveedor__nombre']
    list_filter = ['estado']
    readonly_fields = ['saldo']