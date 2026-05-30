from django import forms
from .models import Persona

class PersonaForm(forms.ModelForm):
    fecha_nacimiento = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control'
        }),
        input_formats=['%Y-%m-%d'],
        required=False
    )
    
    class Meta:
        model = Persona
        fields = ['Nombres', 'edad', 'email', 'fecha_nacimiento', 'parentesco', 'ocupacion', 'datos_medicos', 'ingreso_mensual', 'gastos_mensuales', 'foto']
        widgets = {
            'Nombres': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Juan Pérez'
            }),
            'edad': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: 30',
                'min': '0',
                'max': '120'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'correo@ejemplo.com'
            }),
            'parentesco': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Padre, Madre, Hijo...'
            }),
            'ocupacion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Ingeniero, Abogado...'
            }),
            'datos_medicos': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Alergias, medicamentos...',
                'rows': 3
            }),
            'ingreso_mensual': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0.00',
                'step': '0.01'
            }),
            'gastos_mensuales': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0.00',
                'step': '0.01'
            }),
            'foto': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            })
        }
