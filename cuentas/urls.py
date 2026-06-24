from django.urls import path
from . import views

urlpatterns = [
    path('huespedes/', views.index_huespedes, name='index_huespedes'),
    path('huespedes/nuevo/', views.nuevo_huesped, name='nuevo_huesped'),
    path('huespedes/eliminar/<int:pk>/', views.eliminar_huesped, name='eliminar_huesped'),
]