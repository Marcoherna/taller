from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistroForm

def registro_usuario(request): # agregado para validar usuarios
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            messages.success(request, 'Registro exitoso')
            return redirect('inicio')
        else:
            messages.error(request,'Error en el registro ')
    else:
        form = RegistroForm()
    return render(request, 'usuarios/registro.html', {'form': form})

def acceso_denegado(request): # agregado para denegar el acceso
    return render(request, 'usuarios/acceso_denegado.html', status=403)
    
def logout_view(request): # agregado para apuntar al inicio al salir
    logout(request)
    return redirect('inicio')