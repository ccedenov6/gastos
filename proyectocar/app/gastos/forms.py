from django import forms
from .models import Gasto

class GastoForm(forms.ModelForm):
    fecha = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control'
        }),
        input_formats=['%Y-%m-%d'],
        help_text='Formato: YYYY-MM-DD'
    )
    
    class Meta:
        model = Gasto
        fields = ['descripcion', 'monto', 'categoria', 'fecha', 'persona', 'imagengasto']
        widgets = {
            'descripcion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Compra de alimentos'
            }),
            'monto': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0.00',
                'step': '0.01'
            }),
            'categoria': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Alimentación'
            }),
            'persona': forms.Select(attrs={
                'class': 'form-select'
            }),
            'imagengasto': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            })
        }
