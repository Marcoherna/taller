from django.db import models

# Create your models here.

class Producto(models.Model): # agregado modelo producto
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

class Servicio(models.Model): # agregado modelo servicio
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    productos_requeridos = models.ManyToManyField(Producto, related_name='servicios')