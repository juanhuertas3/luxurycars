from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from gestionventas.models import *
from gestionventas.forms import *

# vistas generales de la app.

def inicio(req):
    return render(req, "gestionventas/inicio.html")

def marcas(req):
    return render(req, "gestionventas/marcas.html") 

def ventas(req):
    return render(req, "gestionventas/ventas.html")

def vendedores(req):
    return render(req, "gestionventas/vendedores.html")
