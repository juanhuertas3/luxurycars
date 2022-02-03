from django.urls import path
from django.urls.conf import include
from gestionventas import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('marcas/', views.marcas, name="marcas"),
    path('ventas/', views.ventas, name="ventas"),
    path('vendedores/', views.vendedores, name="vendedores"),
    path('buscarmarca/', views.buscarmarca, name="buscarmarca"),
    path('buscar/', views.buscar),
    path('leermarcas/', views.leermarcas, name="leermarcas"),
    path('borrarmarca/<id_marca>/', views.borrarmarca, name="borrarmarca"),
    path('nosotros/', views.nosotros, name="nosotros"),
    path('blogpost/', views.blogpost, name="blogpost"),
    
]