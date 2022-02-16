from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView 
from django.views.generic import ListView
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from gestionventas.models import *
from gestionventas.forms import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

### INSTANCIAS DE PAGINAS Y SECCIONES DE LA WEB
def inicio(req):
    return render(req, "gestionventas/inicio.html")

def nosotros(req):
    return render(req, "gestionventas/quienessomos.html")

def blogpost(req):
    return render(req, "gestionventas/blogpost.html") 

def marcas(request):    
    return render (request, "gestionventas/marcas.html")

### INSTANCIA PARA CREAR NUEVOS VENDEDORES EN EL MODELO
@login_required
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

### INSTANCIAS DEL CRUD COMPLETO
class ListarVendedores(LoginRequiredMixin, ListView):
    model= vendedore
    template_name="gestionventas/listar.html" 

class DetalleVendedores(LoginRequiredMixin, DetailView):
    model= vendedore
    template_name="gestionventas/detalles.html"

class CrearVendedores(LoginRequiredMixin, CreateView):
    model= vendedore
    success_url="/gestionventas/listaVendedores/"
    fields=["nombre_vendedor", "apellido_vendedor", "email_vendedor", "sucursal"] 
    template_name ="gestionventas/vendedores.html"

class ModificarVendedores(LoginRequiredMixin, UpdateView):
    model= vendedore
    success_url="/gestionventas/listaVendedores/"
    fields=['nombre_vendedor', 'apellido_vendedor', 'email_vendedor', 'sucursal']
    template_name ="gestionventas/editar.html"

class BorrarVendedores(DeleteView):
    model= vendedore
    success_url="/gestionventas/listaVendedores/"
    template_name ="gestionventas/borrar.html"

### INSTANCIA DE LOGIN
def login_request(request):

    if (request.method == "POST"):
            
            form = AuthenticationForm(request, data = request.POST)
                    
            if form.is_valid():
                  data = form.cleaned_data
                    
                  user = authenticate(username=data['username'], password=data['password'])

                  if user is not None:
                    login(request, user)   
                    
                    return render(request,"gestionventas/inicio.html",  {"mensaje":f"Bienvenido {user.get_username()} Que tal tu dia 😎"} )
                  
                  else:

                    return render(request,"gestionventas/inicio.html", {"mensaje":"Error, datos incorrectos"} )

            else:                        
                return render(request,"gestionventas/inicio.html" ,  {"mensaje":"Error, El usuario no existe o la contraseña esta mal 😥"})
    else:
      form = AuthenticationForm()
      return render(request,"gestionventas/login.html", {'form':form} )

### INSTANCIA PARA CREAR USUARIOS
def register(request):

      if (request.method == "POST"):

            form = UserCreationForm(request.POST)
            
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"gestionventas/inicio.html",   {"mensaje": "Se ha creado exitosamente su usuario, Bienvenido a bordo marinero 😎"} )

      else:
            form = UserCreationForm()       
         

      return render(request,"gestionventas/registro.html" ,  {"form":form})

### INSTANCIA PARA EDITAR PERFIL
@login_required
def editarPerfil(request):

      usuario = request.user
     
      if (request.method == 'POST'):
            miFormulario = UserEditForm(request.POST) 
            if miFormulario.is_valid(): 

                  informacion = miFormulario.cleaned_data
            
                  usuario.email = informacion['email']
                  usuario.password1 = informacion['password1']
                  usuario.password2 = informacion['password2']
                  usuario.last_name = informacion['last_name']
                  usuario.first_name = informacion['first_name']
                  usuario.save()

                  return render(request, "gestionventas/inicio.html") 
      else: 
            miFormulario= UserEditForm(initial={'email':usuario.email, 'last_name':usuario.last_name, 'first_name':usuario.first_name}) 

      return render(request, "gestionventas/editarperfil.html", {"miFormulario":miFormulario, "usuario":usuario})
