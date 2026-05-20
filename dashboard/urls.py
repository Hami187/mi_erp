from django.urls import path
from . import views

urlpatterns = [
    path('', views.hub, name='hub'),
    path('dashboard/', views.index, name='dashboard'),
]