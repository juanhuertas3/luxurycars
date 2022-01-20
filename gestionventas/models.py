from django.db import models

# Create your models here.

class marcasvehiculo(models.Model):
    marca=models.CharField(max_length=25)
    serie=models.CharField(max_length=25)
    ano_fabricacion=models.IntegerField()
    pais_fabricacion=models.CharField(max_length=25)
    
    def __str__(self):
        return f"{self.marca} - ({self.serie}) {self.ano_fabricacion}"

class vendedore(models.Model):
    nombre_vendedor=models.CharField(max_length=35)
    apellido_vendedor=models.CharField(max_length=35)
    email_vendedor=models.EmailField(max_length=30)
    sucursal=models.CharField(max_length=30)

    def __str__(self):
        return f"{self.nombre_vendedor} {self.apellido_vendedor} - ({self.email_vendedor})" 

class venta(models.Model):
    vehiculo_vendido= models.CharField(max_length=30)
    precio=models.IntegerField()
    garantia_tiempo=models.IntegerField()
    garantia_kilometros= models.IntegerField()

    def __str__(self):
        return f"{self.vehiculo_vendido} - ($ {self.precio})"   