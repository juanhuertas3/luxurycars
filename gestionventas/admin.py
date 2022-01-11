from django.contrib import admin
from gestionventas.models import marcasvehiculo, vendedore, venta

# Register your models here.
admin.site.register(marcasvehiculo)
admin.site.register(vendedore)
admin.site.register(venta)
