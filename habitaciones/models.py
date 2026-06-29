from django.db import models
from django.utils import timezone
from datetime import date

# Create your models here.

# Tipos de habitaciones que cuenta el hotel
class Tipo(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        ordering = ['nombre']
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'

class Servicio(models.Model):
    nombre = models.CharField(max_length=100, default='Desayuno')
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    descripcion = models.TextField()
    fecha = models.DateField(default=date.today(), null=True, blank=True)

    def __str__(self):
        return f"{ self.nombre } a Bs. { self.precio }"
    
    class Meta:
        ordering = ['nombre']

class Habitacion(models.Model):
    numero = models.SmallIntegerField()
    piso = models.SmallIntegerField()
    estado = models.CharField(max_length=50, default='Disponible')
    precio = models.DecimalField(decimal_places=6, max_digits=12) # 9999.999999
    telefono = models.CharField(max_length=4, default='1000', blank=True, null=True)
    descripcion = models.TextField()
    banio = models.BooleanField(default=True)
    tipo = models.ForeignKey(Tipo, on_delete=models.PROTECT, related_name="habitaciones")
    servicios = models.ManyToManyField(Servicio, through='HabitacionServicio', related_name='habitaciones')

    def __str__(self):
        return f"Habitacion: piso { self.piso } numero { self.numero }"

    class Meta:
        ordering = ['piso', 'numero']
        verbose_name_plural = 'Habitaciones'

class HabitacionServicio(models.Model):
    cantidad = models.SmallIntegerField(default=1)
    from django.utils import timezone
    fecha = models.DateField(default=timezone.localdate, null=True, blank=True)
   # fecha = models.DateTimeField(default=timezone.now)
    habitacion = models.ForeignKey(Habitacion, on_delete=models.PROTECT, related_name="habitacioneservicios")
    servicio = models.ForeignKey(Servicio, on_delete=models.PROTECT, related_name='habitacionservicios')

    def __str__(self):
        return f"{ self.habitacion} - {self.servicio}, {self.fecha}"