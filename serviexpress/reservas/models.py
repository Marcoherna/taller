from django.db import models
from usuarios.models import Usuario
from servicios.models import Servicio

# Create your models here.

class Reserva(models.Model): # agregado modelo reserva
    ESTADOS = (
        ('pendiente', 'Pendiente'),
        ('aceptada', 'Aceptada'),
        ('rechazada', 'Rechazada'),
        ('completada', 'Completada')
    )
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='reservas')
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, related_name='reservas_atendidas')
    fecha = models.DateTimeField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')

class Boleta(models.Model): # agregado modelo boleta
    reserva = models.OneToOneField(Reserva, on_delete=models.CASCADE)
    fecha_emision = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    
    def calcular_total(self):
        return self.reserva.servicio.precio