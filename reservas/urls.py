from django.urls import path
from . import views

urlpatterns = [
    # Rutas para Reservas
    path('', views.index_reservas, name='index_reservas'),
    path('nueva/', views.nueva_reserva, name='nueva_reserva'),
    
    # Rutas para Pagos
    path('pagos/', views.index_pagos, name='index_pagos'),
    path('pagos/nuevo/', views.nuevo_pago, name='nuevo_pago'),
    path('eliminar/<int:pk>/', views.eliminar_reserva, name='eliminar_reserva'),
]