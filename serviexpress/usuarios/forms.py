from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django.core.validators import RegexValidator, validate_email
from django.core.exceptions import ValidationError

class RegistroForm(UserCreationForm):  # agregado forma del formulatrio registro de usuario
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password1', 'password2', 'rol', 'telefono']
        telefono = forms.CharField(
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$', 
                message="Formato de teléfono inválido"
            )
        ]
    )
    
    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            validate_email(email)
        except ValidationError:
            raise forms.ValidationError("Email inválido")
        
        # Prevenir emails duplicados
        if Usuario.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email ya está registrado")
        return email