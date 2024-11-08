# usuarios/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

def register_view(request):
    # Utiliza el formulario estándar de creación de usuario
    form = UserCreationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()  # Guarda el nuevo usuario
        login(request, user)  # Inicia sesión automáticamente después del registro
        messages.success(request, "Registro exitoso. Bienvenido, ¡has iniciado sesión!")
        return redirect("core:lista_productos")  # Redirige a la página principal de productos
    return render(request, "usuarios/register.html", {"form": form})

def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Bienvenido {user.username}")
            return redirect("core:lista_productos")  # Redirige a la página principal de productos
        else:
            messages.error(request, "Nombre de usuario o contraseña incorrectos.")
    return render(request, "usuarios/login.html", {"form": form})

def logout_view(request):
    logout(request)
    messages.success(request, "Has cerrado sesión correctamente.")
    return redirect("core:lista_productos")  # Redirige a la página principal de productos después del cierre de sesión
