from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Reserva, Servicio
from .forms import ReservaForm

@login_required
def crear_reserva(request, servicio_id):
    servicio = get_object_or_404(Servicio, pk=servicio_id)
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.cliente = request.user
            reserva.servicio = servicio
            reserva.save()
            messages.success(request, 'Reserva creada exitosamente')
            return redirect('reservas:historial')
    else:
        form = ReservaForm()
    return render(request, 'reservas/crear_reserva.html', {'servicio': servicio, 'form': form})

@login_required
def historial_reservas(request):
    reservas = Reserva.objects.filter(cliente=request.user)
    return render(request, 'reservas/historial_reservas.html', {'reservas': reservas})

@login_required
def reservas_pendientes(request):
    reservas = Reserva.objects.filter(estado='pendiente')
    return render(request, 'reservas/reservas_pendientes.html', {'reservas': reservas})

@login_required
def cancelar_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, pk=reserva_id)
    if reserva.cliente == request.user and reserva.estado == 'pendiente':
        reserva.estado = 'cancelada'
        reserva.save()
        messages.success(request, 'Reserva cancelada exitosamente')
    return redirect('reservas:historial')

@login_required
def informe_ventas(request):
    reservas = Reserva.objects.filter(estado='completada')
    total_ventas = sum(reserva.servicio.precio for reserva in reservas)
    return render(request, 'reservas/informe_ventas.html', {
        'reservas': reservas,
        'total_ventas': total_ventas
    })