from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class fMarcas(forms.Form):
    marca=forms.CharField()
    serie=forms.CharField()
    ano_fabricacion=forms.IntegerField()
    pais_fabricacion=forms.CharField()

class fVentas(forms.Form):
    vehiculo_vendido= forms.CharField()
    precio=forms.IntegerField()
    garantia_tiempo=forms.IntegerField()
    garantia_kilometros= forms.IntegerField()

class fVendedores(forms.Form):
    nombre_vendedor=forms.CharField()
    apellido_vendedor=forms.CharField()
    email_vendedor=forms.EmailField()
    sucursal=forms.CharField()

class UserEditForm(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 
    first_name = forms.CharField()
    last_name = forms.CharField()
    imagen_avatar = forms.ImageField(required=False) 

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name'] 
        #Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}