from django.contrib import admin
from .models import Pago, Reserva

# Register your models here.

admin.site.register([
    Pago,
    Reserva
])