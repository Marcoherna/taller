from django.contrib import admin
from .models import Reserva, Boleta

# Register your models here.


admin.site.register(Reserva) # agregado el registro de modelo reserva
admin.site.register(Boleta) # agregado el registro de modelo boleta