from django import forms
from datetime import date
from .models import Reserva, Pago

class FormReservaNew(forms.ModelForm):
    class Meta:
        model = Reserva
        # Usamos los campos exactos de tu modelo
        fields = ['habitaciones', 'huspedes', 'fecha_inicio', 'fecha_salida']
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date', 'min': date.today().strftime('%Y-%m-%d')}),
            'fecha_salida': forms.DateInput(attrs={'type': 'date', 'min': date.today().strftime('%Y-%m-%d')}),
            # Al ser ManyToMany, estos campos se seleccionan mejor manteniendo presionada la tecla Ctrl
            'habitaciones': forms.SelectMultiple(attrs={'style': 'width: 100%; height: 100px;'}),
            'huspedes': forms.SelectMultiple(attrs={'style': 'width: 100%; height: 100px;'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        fecha_inicio = cleaned_data.get('fecha_inicio')
        fecha_salida = cleaned_data.get('fecha_salida')

        if fecha_inicio and fecha_salida and fecha_salida < fecha_inicio:
            raise forms.ValidationError("La fecha de salida no puede ser anterior a la fecha de inicio.")
        return cleaned_data

class FormPagoNew(forms.ModelForm):
    class Meta:
        model = Pago
        # Usamos los campos exactos de tu modelo Pago
        fields = ['reserva', 'monto', 'tipo', 'descripcion']
        widgets = {
            'monto': forms.NumberInput(attrs={'step': '0.01', 'min': '0.00'}),
            'descripcion': forms.Textarea(attrs={'cols': 40, 'rows': 3, 'placeholder': 'Ej. Pago total de la estadía...'}),
        }