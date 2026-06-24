from django import forms
from .models import Huesped
from django.utils import timezone

class FormHuespedNew(forms.ModelForm):
    class Meta:
        model = Huesped
        # Campos exactos de tu modelo Huesped
        fields = ['nombres', 'paterno', 'materno', 'ci', 'complemento', 'origen', 'telefono', 'fecha_nacimiento', 'email']
        widgets = {
            'nombres': forms.TextInput(attrs={'placeholder': 'Nombres completos'}),
            'paterno': forms.TextInput(attrs={'placeholder': 'Apellido Paterno (Opcional)'}),
            'materno': forms.TextInput(attrs={'placeholder': 'Apellido Materno'}),
            'ci': forms.TextInput(attrs={'placeholder': 'Nro. Documento'}),
            'complemento': forms.TextInput(attrs={'placeholder': 'Ej. 1F (Si tiene)', 'maxlength': '2'}),
            'origen': forms.TextInput(attrs={'placeholder': 'Ej. Potosí, LP, CBBA...'}),
            'telefono': forms.TextInput(attrs={'placeholder': 'Ej. 71234567', 'maxlength': '8'}),
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
            'email': forms.EmailInput(attrs={'placeholder': 'correo@ejemplo.com'}),
        }