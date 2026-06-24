from django.contrib import admin
from .models import Habitacion, Tipo, Servicio

# Register your models here.

admin.site.register([
    Habitacion,
    Tipo,
    Servicio,
])