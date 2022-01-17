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

def form_marcas(request):
    miformulario = Form_Marcas(request.POST)
    print(miformulario)

    if miformulario.is_valid():
        info = miformulario.cleaned_data
        marca = marcasvehiculo (marca=info['marca'], serie=info['serie'], ano_fabricacion=info['ano_fabricacion'], pais_fabricacion=info['pais_fabricacion'],)
        marca.save()

        return render(request, "gestionventas/marcas.html")
    
    else:
        miformulario = Form_Marcas()
    
    return render (request, "gestionventas/formulario_marcas.html", {"miformulario":miformulario})

def form_ventas(request):
    miformulario2 = Form_Ventas(request.POST)
    print(miformulario2)

    if miformulario2.is_valid():
        info = miformulario2.cleaned_data
        ventas = venta (vehiculo_vendido=info['vehiculo_vendido'], precio=info['precio'], garantia_tiempo=info['garantia_tiempo'], garantia_kilometros=info['garantia_kilometros'],)
        ventas.save()

        return render(request, "gestionventas/ventas.html")
    
    else:
        miformulario2 = Form_Ventas()
    
    return render (request, "gestionventas/formulario_ventas.html", {"miformulario2":miformulario2})

def form_vendedores(request):
    miformulario3 = Form_Vendedores(request.POST)
    print(miformulario3)

    if miformulario3.is_valid():
        info = miformulario3.cleaned_data
        vendedor = vendedore (nombre_vendedor=info['nombre_vendedor'], apellido_vendedor=info['apellido_vendedor'], email_vendedor=info['email_vendedor'], sucursal=info['sucursal'],)
        vendedor.save()

        return render(request, "gestionventas/vendedores.html")
    
    else:
        miformulario3 = Form_Vendedores()
    
    return render (request, "gestionventas/formulario_vendedores.html", {"miformulario3":miformulario3})
