from django.urls import path
from .views import inicio

urlpatterns = [
    path('', inicio, name='inicio'), # agregado para mostrar inicio.html
]