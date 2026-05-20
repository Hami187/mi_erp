from django.urls import path
from . import views, reportes

urlpatterns = [
    path('', views.lista_ventas, name='lista_ventas'),
    path('nuevo/', views.crear_venta, name='crear_venta'),
    path('<int:pk>/', views.detalle_venta, name='detalle_venta'),
    path('<int:pk>/eliminar/', views.eliminar_venta, name='eliminar_venta'),
    path('pdf/<int:venta_id>/', reportes.generar_pdf_venta, name='venta_pdf'),
]