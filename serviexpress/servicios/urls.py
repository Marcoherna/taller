from django.urls import path
from .views import lista_servicios, crear_servicio, editar_servicio

app_name = 'servicios'

urlpatterns = [
    path('', lista_servicios, name='lista'), # agregado para mostrar lista.html
    path('crear/', crear_servicio, name='crear'), # agregado para mostrar crear_servicio.html
    path('editar/<int:pk>/', editar_servicio, name='editar'), # agregado para ...
]