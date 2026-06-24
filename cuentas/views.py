from django.shortcuts import render, redirect, get_object_or_404
from .models import Huesped
from .forms import FormHuespedNew

def index_huespedes(request):
    huespedes = Huesped.objects.all().order_by('paterno')
    # Usamos tu estructura limpia y ordenada
    return render(request, 'cuentas/huespedes.html', {'huespedes': huespedes})

def nuevo_huesped(request):
    if request.method == 'POST':
        form = FormHuespedNew(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index_huespedes')
    else:
        form = FormHuespedNew()
    return render(request, 'cuentas/nuevo_huesped.html', {'form': form})

def eliminar_huesped(request, pk):
    huesped = get_object_or_404(Huesped, pk=pk)
    huesped.delete()
    return redirect('index_huespedes')