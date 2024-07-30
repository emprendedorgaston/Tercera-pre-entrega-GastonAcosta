from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistroForm
from django.urls import reverse_lazy

class CustomLoginView(LoginView):
    template_name = 'user/inicio_sesion.html'
    redirect_authenticated_user = True

    def form_valid(self, form):
        """If the form is valid, redirect to the supplied URL."""
        messages.info(self.request, f"Has iniciado sesión como {form.get_user().username}.")
        return super().form_valid(form)

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form with error messages."""
        messages.error(self.request, "Usuario o contraseña incorrectos.")
        return super().form_invalid(form)

class CustomLogoutView(LogoutView):
    template_name = 'user/logout.html'

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, "Has cerrado sesión exitosamente.")
        return super().dispatch(request, *args, **kwargs)

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Bienvenido {user.username}, tu registro ha sido exitoso.")
            return redirect('lista_productos')
        else:
            messages.error(request, "Por favor, corrija los errores.")
    else:
        form = RegistroForm()
    return render(request, 'user/registro.html', {'form': form})

def inicio_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Has iniciado sesión como {username}.")
                return redirect('lista_productos')
            else:
                messages.error(request, "Usuario o contraseña incorrectos.")
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")
    else:
        form = AuthenticationForm()
    return render(request, 'user/inicio_sesion.html', {'form': form})

def cerrar_sesion(request):
    logout(request)
    messages.info(request, "Has cerrado sesión exitosamente.")
    return redirect('inicio_sesion')
