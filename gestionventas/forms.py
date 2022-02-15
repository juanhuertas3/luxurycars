from django import forms

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

