from django.urls import path
from .views import (
    crear_reserva, 
    historial_reservas, 
    reservas_pendientes, 
    cancelar_reserva, 
    informe_ventas
)

app_name = 'reservas'

urlpatterns = [
    path('crear/<int:servicio_id>/', crear_reserva, name='crear'),
    path('historial/', historial_reservas, name='historial'),
    path('pendientes/', reservas_pendientes, name='pendientes'),
    path('cancelar/<int:reserva_id>/', cancelar_reserva, name='cancelar'),
    path('informes/', informe_ventas, name='informes'),
]