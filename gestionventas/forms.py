from django import forms

class Form_Marcas(forms.Form):
    marca=forms.CharField()
    serie=forms.CharField()
    ano_fabricacion=forms.IntegerField()
    pais_fabricacion=forms.CharField()

class Form_Ventas(forms.Form):
    vehiculo_vendido= forms.CharField()
    precio=forms.IntegerField()
    garantia_tiempo=forms.IntegerField()
    garantia_kilometros= forms.IntegerField()

class Form_Vendedores(forms.Form):
    nombre_vendedor=forms.CharField()
    apellido_vendedor=forms.CharField()
    email_vendedor=forms.EmailField()
    sucursal=forms.CharField()