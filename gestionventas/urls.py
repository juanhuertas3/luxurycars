from django.urls import path
from django.urls.conf import include
from gestionventas import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('nosotros/', views.nosotros, name="nosotros"),
    path('blogpost/', views.blogpost, name="blogpost"),
    path('marcas/', views.marcas, name="marcas"),
    path('vendedores/', views.vendedores, name="vendedores"),
    path('login/', views.login_request, name="login"),
    path('listaVendedores/', views.ListarVendedores.as_view(), name="listar"),
    path('detalle/<pk>/', views.DetalleVendedores.as_view(), name='Detalle'),
    path('nuevo', views.CrearVendedores.as_view(), name='Nuevo'),
    path('modificar/<pk>/', views.ModificarVendedores.as_view(), name='Modificar'),
    path('eliminar/<pk>/', views.BorrarVendedores.as_view(), name='Eliminar'), 
    path('registrar/', views.register, name='registrar'), 
    path('logout/', LogoutView.as_view(template_name='gestionventas/logout.html'), name='logout'), 
    path('editarperfil/', views.editarPerfil, name='editarperfil'), 

]