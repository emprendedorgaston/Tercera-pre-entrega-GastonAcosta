from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroForm(UserCreationForm):
    nombre = forms.CharField(max_length=100, required=True, help_text='Requerido. 100 caracteres o menos.')
    apellido = forms.CharField(max_length=100, required=True, help_text='Requerido. 100 caracteres o menos.')
    dni = forms.CharField(max_length=20, required=True, help_text='Requerido. 20 caracteres o menos.')
    email = forms.EmailField(required=True, help_text='Requerido. Introduce una dirección de correo válida.')

    class Meta:
        model = User
        fields = ['username', 'nombre', 'apellido', 'dni', 'email', 'password1', 'password2']
        labels = {
            'username': 'Nombre de usuario',
            'password1': 'Contraseña',
            'password2': 'Confirmar contraseña',
        }
        help_texts = {
            'username': 'Requerido. 150 caracteres o menos. Letras, dígitos y @/./+/-/_ solamente.',
        }
        error_messages = {
            'username': {
                'unique': "Un usuario con ese nombre ya existe.",
            },
            'email': {
                'unique': "Ya existe un usuario con esa dirección de correo.",
            },
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Ya existe un usuario con esa dirección de correo.")
        return email


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
