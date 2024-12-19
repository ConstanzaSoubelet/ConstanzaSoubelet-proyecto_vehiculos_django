from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Vehiculo
from .forms import VehiculoForm

def index(request):
    if request.user.is_authenticated:
        return render(request, 'vehiculo/index.html', {'title': 'Catálogo de Vehículos'})
    else:
        if request.method == 'POST':
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect('index')
        else:
            form = AuthenticationForm()
        return render(request, 'vehiculo/index.html', {'form': form, 'title': 'Catálogo de Vehículos'})

def logout_view(request):
    logout(request)
    return redirect('index')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'vehiculo/login.html', {'form': form})

def add_vehiculo(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_vehiculos')
    else:
        form = VehiculoForm()
    
    return render(request, 'vehiculo/add_vehiculo.html', {'form': form})

def listar_vehiculos(request):
    if not request.user.is_authenticated:
        return redirect('login')

    vehiculos = Vehiculo.objects.all()
    return render(request, 'vehiculo/listar_vehiculos.html', {'vehiculos': vehiculos})
