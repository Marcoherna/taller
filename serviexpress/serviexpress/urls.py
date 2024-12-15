from django.urls import path, include
from django.contrib import admin
from usuarios.views import acceso_denegado

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('usuarios/', include('usuarios.urls')), # agregado
    path('servicios/', include(('servicios.urls', 'servicios'), namespace='servicios')), # agregado
    path('reservas/', include(('reservas.urls', 'reservas'), namespace='reservas')), # agregado
    path('acceso-denegado/', acceso_denegado, name='acceso_denegado'), # agregado
]