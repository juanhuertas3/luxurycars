from django.db import models

# Create your models here.

class marcasvehiculos(models.Model):
    marca=models.CharField(max_length=25)
    serie=models.CharField(max_length=25)
    ano_fabricacion=models.IntegerField(max_length=4)
    pais_fabricacion=models.CharField(max_length=25)
    Precio=models.IntegerField()

class vendedor(models.Model):
    nombre_vendedor=models.CharField(max_length=35)
    apellido_vendedor=models.CharField(max_length=35)
    email_vendedor=models.EmailField(max_length=30)
    sucursal=models.CharField(max_length=30)