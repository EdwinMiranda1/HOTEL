from django import forms
from datetime import datetime, date
from .models import Habitacion, Tipo
from django.utils import timezone

class FormServicioNew(forms.Form):
    nombre = forms.CharField(max_length=50, required=True, initial='Desayuno', label='Nombres', help_text="Nombre del servicio")
    precio = forms.DecimalField(
        max_digits=8,
        decimal_places=2,
        label='Precio',
        initial=20,
        required=True,
        widget=forms.NumberInput(attrs={'step': '0.01', 'min': '0.00'}),
        error_messages={
            'max_digits': 'El precio no puede tener mas de seis digitos',
            'max_decimales_digits': 'La parte decimal solo debe contener dos digitos',
            'max_whole_digits': 'La parte entera del precio no puede ser mayor a 9999'
        }
    )
    descripcion = forms.CharField(
        initial='Desayuno completo',
        label='Descripcion',
        required=False,
        widget=forms.Textarea(attrs={'cols': 50, 'rows': 15, 'class': 'area_texto'})
    )
    fecha = forms.DateField(
    initial=timezone.localdate(),
    widget=forms.DateInput(attrs={'type': 'date'})
    )


    def clean_fecha(self):
        fecha = self.cleaned_data["fecha"]
        if fecha < timezone.localdate():
            raise forms.ValidationError("El servicio no puede ser en pasado")
        return fecha
    
    # def clean_precio(self):


class FormHabitacionEdit(forms.ModelForm):
    class Meta:
        model = Habitacion
        fields = ['id', 'estado', 'precio', 'descripcion', 'banio', 'tipo']

class FormTipoNew(forms.ModelForm):
    class Meta:
        model = Tipo
        fields = '__all__'