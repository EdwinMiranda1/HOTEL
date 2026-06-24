from django.db import models
from django.utils import timezone
from datetime import date
from cuentas.models import Huesped
from habitaciones.models import Habitacion

# Create your models here.

class Reserva(models.Model):
    fecha = models.DateTimeField(default=timezone.now)
    fecha_inicio = models.DateField(default=timezone.now)
    fecha_salida = models.DateField(default=timezone.now)

    huspedes = models.ManyToManyField(Huesped, related_name='reservas')
    habitaciones = models.ManyToManyField(Habitacion, related_name='reservas')

    def __str__(self):
        return f"{ self.fecha_inicio } ({ self.habitaciones })"
    
    class Meta:
        ordering = ['-fecha_inicio']

class Pago(models.Model):
    monto = models.DecimalField(max_digits=9, decimal_places=2) # 9999999.99
    fecha = models.DateTimeField(default=timezone.now)
    descripcion = models.TextField()

    TIPOS_CHOICES_PAGO = {
        'efectivo': 'EFECTIVO',
        'qr': 'QR',
        'tarjeta': 'TARJETA DEBITO/CREDITO',
        'transferencia': 'TRANSFENCIA',
    }

    tipo = models.CharField(max_length=25, choices=TIPOS_CHOICES_PAGO, default='efectivo')

    reserva = models.ForeignKey(Reserva, on_delete=models.PROTECT, related_name="pagos", null=True, blank=True)
    def __str__(self):
        return f"{ self.fecha } Bs. { self.monto } por { self.descripcion}"

    class Meta:
        ordering = ['-fecha']