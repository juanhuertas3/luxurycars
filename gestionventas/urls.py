from django.urls import path
from django.urls.conf import include
from gestionventas import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('marcas/', views.marcas, name="marcas"),
    path('ventas/', views.ventas, name="ventas"),
    path('vendedores/', views.vendedores, name="vendedores"),
    path('formulario_marcas/', views.form_marcas, name="formulario_marcas"),
    path('formulario_ventas/', views.form_ventas, name="formulario_ventas"),
    path('formulario_vendedores/', views.form_vendedores, name="formulario_vendedores"),
    path('buscarmarca/', views.buscarmarca, name="buscarmarca"),
    path('buscar/', views.buscar),

]