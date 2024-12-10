from django.urls import path
from django.contrib.auth import views as auth_views
from .views import registro_usuario, acceso_denegado, logout_view

urlpatterns = [
    path('registro/', registro_usuario, name='registro'),
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
    path('acceso-denegado/', acceso_denegado, name='acceso_denegado'),
]