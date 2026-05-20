from django.contrib import admin
from .models import Departamento, Empleado, Nomina


@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion']
    search_fields = ['nombre']


@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ['cedula', 'nombre', 'apellido', 'departamento', 'cargo', 'salario', 'estado']
    search_fields = ['cedula', 'nombre', 'apellido']
    list_filter = ['departamento', 'estado']


@admin.register(Nomina)
class NominaAdmin(admin.ModelAdmin):
    list_display = ['empleado', 'mes', 'anio', 'salario_base', 'bonificaciones', 'descuentos', 'total', 'estado']
    search_fields = ['empleado__nombre', 'empleado__apellido']
    list_filter = ['estado', 'anio', 'mes']
    readonly_fields = ['total']