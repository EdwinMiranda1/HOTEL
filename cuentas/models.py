from django.db import models
from datetime import date
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Huesped(models.Model):
    nombres = models.CharField(max_length=25)
    paterno = models.CharField(max_length=15, blank=True, null=True)
    materno = models.CharField(max_length=15)
    ci = models.CharField(max_length=13, unique=True)
    complemento = models.CharField(max_length=2, blank=True, null=True)
    origen = models.CharField(max_length=20)
    telefono = models.CharField(max_length=8, null=True, blank=True)
    fecha_nacimiento = models.DateField(default=timezone.now)
    email = models.CharField(max_length=50, unique=True, null=True, blank=True)

    def __str__(self):
        if self.paterno is None:
            return f"{self.materno} {self.nombres}"
        else:
            return f"{self.paterno} {self.materno} {self.nombres}"
    
    class Meta:
        ordering = ['paterno', 'materno', 'nombres']
        verbose_name_plural = 'Huespedes'

class Rol(models.Model):
    nombre = models.CharField(max_length=20, default='Secretaria')

    def __str__(self):
        return self.nombre
    
    class Meta:
        ordering = ['nombre']
        verbose_name_plural = 'Roles'

class Usuario(AbstractUser):
    # username, password, last_login, is_superuser, last_name, email, is_staff, is_active, date_joined, firt_name
    rol = models.ForeignKey(Rol, on_delete=models.PROTECT, related_name='usuarios', null=True, blank=True)
    huesped = models.OneToOneField(Huesped, on_delete=models.PROTECT, related_name='usuario', null=True, blank=True)

    def __str__(self):
        return f"{ self.username } - { self.huesped }"
