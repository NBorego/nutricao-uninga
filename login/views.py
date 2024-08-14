from django.shortcuts import render, redirect
from .forms import *

# Create your views here.
def tipo_login(request):
    return render(request, 'login/tipo_login.html')

def login_cliente(request):
    if request.method == 'POST':
        form = ClienteLoginForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login_cliente')
    else: 
        form = ClienteLoginForm()

        return render(request, 'login/login_cliente.html', {'form': form})
    
def login_nutricionista(request):
    if request.method == 'POST':
        form = NutricionistaLoginForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login_nutricionista')
    else: 
        form = NutricionistaLoginForm()
        return render(request, 'login/login_nutricionista.html', {'form': form})
    
def registrar_cliente(request):
    if request.method == 'POST':
        form = RegistrarClienteForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('registrar_cliente')
    else:
        form = RegistrarClienteForm()
        return render(request, 'login/registrar_cliente.html', {'form': form})

def registrar_nutricionista(request):
    if request.method == 'POST':
        form = RegistrarNutricionistaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('registrar_cliente')
    else:
        form = RegistrarNutricionistaForm()
        return render(request, 'login/adm/registrar_nutricionista.html', {'form': form})

def logar_adm(request):
    return render(request, 'login/adm/logar_adm.html')
