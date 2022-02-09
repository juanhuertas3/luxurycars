from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from gestionventas.models import *
from gestionventas.forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
# vistas generales de la app.

def inicio(req):
    return render(req, "gestionventas/inicio.html")

def marcas(request):
    miformulario = fMarcas(request.POST)
    print(miformulario)

    if miformulario.is_valid():
        info = miformulario.cleaned_data
        marca = marcasvehiculo (marca=info['marca'], serie=info['serie'], ano_fabricacion=info['ano_fabricacion'], pais_fabricacion=info['pais_fabricacion'],)
        marca.save()

        return render(request, "gestionventas/marcas.html")
    
    else:
        miformulario = fMarcas()
    
    return render (request, "gestionventas/marcas.html", {"miformulario":miformulario})

def ventas(request):
    miformulario2 = fVentas(request.POST)
    print(miformulario2)

    if miformulario2.is_valid():
        info = miformulario2.cleaned_data
        ventas = venta (vehiculo_vendido=info['vehiculo_vendido'], precio=info['precio'], garantia_tiempo=info['garantia_tiempo'], garantia_kilometros=info['garantia_kilometros'],)
        ventas.save()

        return render(request, "gestionventas/ventas.html")
    
    else:
        miformulario2 = fVentas()
    
    return render (request, "gestionventas/ventas.html", {"miformulario2":miformulario2})

def vendedores(request):
    miformulario3 = fVendedores(request.POST)
    print(miformulario3)

    if miformulario3.is_valid():
        info = miformulario3.cleaned_data
        vendedor = vendedore (nombre_vendedor=info['nombre_vendedor'], apellido_vendedor=info['apellido_vendedor'], email_vendedor=info['email_vendedor'], sucursal=info['sucursal'],)
        vendedor.save()

        return render(request, "gestionventas/vendedores.html")
    
    else:
        miformulario3 = fVendedores()
    
    return render (request, "gestionventas/vendedores.html", {"miformulario3":miformulario3})

def buscarmarca(request):
    
    return render(request, "gestionventas/busquedamarca.html/")

def buscar(request):

    if request.GET ["marca"]:
        marcas = request.GET["marca"]
        marca = marcasvehiculo.objects.filter(marca__icontains=marcas)

        return render (request, "gestionventas/resultadosbusqueda.html", {"marca": marca})
        
    else:
        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)

def leermarcas(request):
    marca = marcasvehiculo.objects.all()
    contexto = {"marca": marca}
    return render (request, "gestionventas/leermarcas.html", contexto)

def borrarmarca(request, id_marca):
    marca= marcasvehiculo.objects.get(id=id_marca)
    marca.delete()

    marcas= marcasvehiculo.objects.all()
    contexto={"marcas":marcas}

    return render(request, "gestionventas/leermarcas.html", contexto)

def nosotros(req):
    return render(req, "gestionventas/quienessomos.html")

def blogpost(req):
    return render(req, "gestionventas/blogpost.html") 

def loginrequest(request):

    if request.method == "POST":
            form = AuthenticationForm(request, data = request.POST)
                    
            if form.is_valid():
                  usuario = form.cleaned_data.get('username')
                  contra = form.cleaned_data.get('password')
                  user = authenticate(username=usuario, password=contra)

                  if user is not None:
                    login(request, user)   
                    return render(request,"gestionventas/inicio.html",  {"mensaje":f"Bienvenido {usuario}"} )
                  
                  else:                        
                    return render(request,"gestionventas/inicio.html", {"mensaje":"Error, datos incorrectos"} )

            else:                        
                return render(request,"gestionventas/inicio.html" ,  {"mensaje":"Error, formulario erroneo"})
    else:
      form = AuthenticationForm()
      return render(request,"gestionventas/login.html", {'form':form} )