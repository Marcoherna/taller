from django import forms
from .models import Reserva
from django.utils import timezone


class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['servicio', 'fecha']
        widgets = {
            'fecha': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }
    def clean_fecha(self):
        fecha = self.cleaned_data['fecha']
        
        # Validar que la fecha no sea en el pasado
        if fecha < timezone.now():
            raise forms.ValidationError("No puedes reservar en el pasado")
        
        # Limitar reservas con 2 días de anticipación
        max_fecha = timezone.now() + timezone.timedelta(days=60)
        if fecha > max_fecha:
            raise forms.ValidationError("Solo puedes reservar con hasta 60 días de anticipación")
        
        return fecha