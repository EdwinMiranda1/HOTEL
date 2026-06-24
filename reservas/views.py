from django.shortcuts import render, redirect, get_object_or_404
from .models import Reserva, Pago
from .forms import FormReservaNew, FormPagoNew

# --- VISTAS DE RESERVAS ---

def index_reservas(request):
    reservas = Reserva.objects.all().order_by('-fecha_inicio')
    return render(request, 'reservas/reservas.html', {'reservas': reservas})

def nueva_reserva(request):
    if request.method == 'POST':
        form = FormReservaNew(request.POST)
        if form.is_valid():
            reserva = form.save()
            for habitacion in reserva.habitaciones.all():
                habitacion.estado = 'Ocupada' # Ajusta 'Ocupada' u 'on' según tus nombres de estado
                habitacion.save()
            return redirect('index_reservas')
    else:
        form = FormReservaNew()
    return render(request, 'reservas/nueva_reserva.html', {'form': form})

def index_pagos(request):
    pagos = Pago.objects.all().order_by('-fecha_pago')
    return render(request, 'pagos/index.html', {'pagos': pagos})

def nuevo_pago(request):
    if request.method == 'POST':
        form = FormPagoNew(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index_pagos')
    else:
        form = FormPagoNew()
    return render(request, 'pagos/nuevo.html', {'form': form})
def eliminar_reserva(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    
    for habitacion in reserva.habitaciones.all():
        habitacion.estado = 'Disponible' 
        habitacion.save()
        
    reserva.delete() 
    return redirect('index_reservas') 
# --- VISTAS DE PAGOS ---

def index_pagos(request):
    pagos = Pago.objects.all().order_by('-fecha')
    # 🌟 Apuntamos a tu estructura limpia:
    return render(request, 'reservas/pagos.html', {'pagos': pagos})

def nuevo_pago(request):
    if request.method == 'POST':
        form = FormPagoNew(request.POST)
        if form.is_valid():
            pago = form.save(commit=False)
            reserva_id = request.POST.get('reserva')  
            if reserva_id:
                reserva_objeto = get_object_or_404(Reserva, pk=reserva_id)
                pago.reserva = reserva_objeto
            pago.save()
            return redirect('index_pagos')
    else:
        form = FormPagoNew()
    return render(request, 'reservas/nuevos_pagos.html', {'form': form})