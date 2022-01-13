from django import forms

class formulario_ventas(forms.Form):
    vehiculo_vendido = forms.CharField()
    precio = forms.CharField()
    garantia_tiempo = forms.IntegerField()
    garantia_kilometros = forms.IntegerField()
