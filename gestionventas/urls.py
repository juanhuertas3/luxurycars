from django.urls import path
from django.urls.conf import include
from gestionventas import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('marcas/', views.marcas, name="marcas"),
    path('ventas/', views.ventas, name="ventas"),
    path('vendedores/', views.vendedores, name="vendedores"),

]

