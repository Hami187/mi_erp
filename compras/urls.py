from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_compras, name='lista_compras'),
    path('nuevo/', views.crear_compra, name='crear_compra'),
    path('<int:pk>/', views.detalle_compra, name='detalle_compra'),
    path('<int:pk>/eliminar/', views.eliminar_compra, name='eliminar_compra'),
]