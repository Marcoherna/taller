from django.urls import path, include
from django.contrib import admin
from usuarios.views import acceso_denegado

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('servicios/', include(('servicios.urls', 'servicios'), namespace='servicios')),
    path('reservas/', include(('reservas.urls', 'reservas'), namespace='reservas')),
    path('acceso-denegado/', acceso_denegado, name='acceso_denegado'),
]