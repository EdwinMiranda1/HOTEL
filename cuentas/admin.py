from django.contrib import admin
from .models import Huesped, Rol, Usuario

# Register your models here.

admin.site.register([
    Huesped,
    Rol,
    Usuario,
])
