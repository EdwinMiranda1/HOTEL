from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_habitaciones, name='index_habitaciones'),
    path('detalles/<int:id>', views.detalles_habitacion, name='detalle_habitacion'),
    path('nueva', views.nueva_habitacion, name='nueva_habitacion'),
    path('editar/<int:id>', views.edit_habitacion, name='edit_habitacion'),
    path('servicios/eliminar/<int:id>/', views.eliminar_servicio, name='eliminar_servicio'),

    # nueva habitacion
    # editar
    # mostrar
    # eliminar
    path('tipos', views.index_tipo, name='index_tipo'),
    path('servicios', views.index_servicio, name='index_servicio'),
    path('servicios/nuevo', views.nuevo_servicio, name='nuevo_servicio'),
    # localhost:8000/habitaciones/servicios/nuevo
]

# 1. url (direccion): dns/apps/url; localhost:8000/habitaciones/tipos
# 2. Vista: index_tipo
# 3. name (nombre de la url), no se puede repetir durante el proyecto, es  decir, es único