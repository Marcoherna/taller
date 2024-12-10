from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Servicio
from .forms import ServicioForm

@login_required
def lista_servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'servicios/lista.html', {'servicios': servicios})

@login_required
def crear_servicio(request):
    if request.method == 'POST':
        form = ServicioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('servicios:admin')
    else:
        form = ServicioForm()
    return render(request, 'servicios/crear_servicio.html', {'form': form})

@login_required
def editar_servicio(request, pk):
    servicio = get_object_or_404(Servicio, pk=pk)
    if request.method == 'POST':
        form = ServicioForm(request.POST, instance=servicio)
        if form.is_valid():
            form.save()
            return redirect('servicios:admin')
    else:
        form = ServicioForm(instance=servicio)
    return render(request, 'servicios/editar_servicio.html', {'form': form})