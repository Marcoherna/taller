from django.urls import path
from .views import (
    crear_reserva, 
    historial_reservas, 
    reservas_pendientes, 
    cancelar_reserva, 
    informe_ventas,
    completar_reserva
)

app_name = 'reservas'

urlpatterns = [
    path('crear/<int:servicio_id>/', crear_reserva, name='crear'), # agregado para crera reservas
    path('historial/', historial_reservas, name='historial'), # agregado para mostrar historial_reservas.html
    path('pendientes/', reservas_pendientes, name='pendientes'), # agregado para mostrar reservas_pendientes.html
    path('cancelar/<int:reserva_id>/', cancelar_reserva, name='cancelar_reserva'), # agregado para mostrar cancelaciones
    path('completar/<int:reserva_id>/', completar_reserva, name='completar_reserva'),
    path('informes/', informe_ventas, name='informes'), # agregado para mostrar informe de ventas
]