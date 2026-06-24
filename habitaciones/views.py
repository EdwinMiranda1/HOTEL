from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Habitacion, Tipo, Servicio
from .forms import FormServicioNew, FormHabitacionEdit, FormTipoNew

# Create your views here.

def index_tipo(request):
    if request.method == 'POST':
        form = FormTipoNew(request.POST)
        if form.is_valid():
            form.save() # Guarda el nuevo tipo (Simple, Doble, etc.)
            return redirect('index_tipo') # Recarga la página para ver los cambios
    else:
        form = FormTipoNew() # Crea el formulario vacío
        
    tipos = Tipo.objects.all() # Trae todos los tipos de la base de datos
    
    # 🌟 Renderiza la plantilla pasándole el formulario y los tipos registrados
    return render(request, 'tipos/tipos_servicio.html', {'tipos': tipos, 'form': form})

def index_habitaciones(request):
    habitaciones = Habitacion.objects.all()
    return render(request, 'habitaciones/index.html', {'habitaciones': habitaciones})

def detalles_habitacion(request, id):
    habitacion = Habitacion.objects.get(pk=id)
    return render(request, 'habitaciones/detalles.html', {'habitacion': habitacion})

def nueva_habitacion(request):
    if request.method == 'GET':
        tipos = Tipo.objects.all()
        return render(request, 'habitaciones/nueva.html', {'tipos': tipos})
    else:
        datos = request.POST
        banio = False
        if 'banio' in datos:
            banio = True
        habitacion = Habitacion.objects.create(
            numero = datos['numero'],
            piso = datos['piso'],
            estado = datos['estado'],
            precio = datos['precio'],
            telefono = datos['telefono'],
            descripcion = datos['descripcion'],
            banio = banio,
            tipo_id = datos['tipo']
        )
        return redirect('index_habitaciones')
    
def index_servicio(request):
    servicios = Servicio.objects.all().order_by('nombre')
    return render(request, 'servicios/index.html')
    
def nuevo_servicio(request):
    if request.method == 'GET':
        form = FormServicioNew()
    else:
        form = FormServicioNew(request.POST)
        if form.is_valid():
            servicio = Servicio.objects.create(
                nombre = form.cleaned_data['nombre'],
                precio = form.cleaned_data['precio'],
                descripcion = form.cleaned_data['descripcion'],
                fecha = form.cleaned_data['fecha']
            )
            # return HttpResponse(form.cleaned_data['precio'])
            return redirect('index_servicio')
    return render(request, 'servicios/nuevo.html', {'form': form})

def edit_habitacion(request, id):
    habitacion = get_object_or_404(Habitacion, pk=id)
    if request.method == 'GET':
        form = FormHabitacionEdit(instance = habitacion)
    else:
        form = FormHabitacionEdit(request.POST, instance=habitacion)
        if form.is_valid():
            form.save()
            return redirect('index_habitaciones')
    return render(request, 'habitaciones/edit.html', {'form': form, 'id': id})