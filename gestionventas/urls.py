from django.urls import path
from django.urls.conf import include
from gestionventas import views

urlpatterns = [
    path('', views.inicio),
    path('marcas/', views.marcas),
    path('ventas/', views.ventas),
    path('vendedores/', views.vendedores),

]


