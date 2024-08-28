from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import ClienteForm, NutricionistaForm, CustomAuthenticationForm

def tipo_login(request):
    return render(request, 'login/tipo_login.html')

def login_cliente(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)

            if user.is_cliente:
                return redirect('pagina_cliente')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login/login_cliente.html', {'form': form})
    
def login_nutricionista(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)

            if user.is_nutricionista:
                return redirect('pagina_nutricionista')
    else: 
        form = CustomAuthenticationForm() 
    
    return render(request, 'login/login_nutricionista.html', {'form': form})
    
def registrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('pagina_cliente')
    else:
        form = ClienteForm()
    return render(request, 'login/registrar_cliente.html', {'form': form})

def registrar_nutricionista(request):
    if request.method == 'POST':
        form = NutricionistaForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('pagina_nutricionista')
    else:
        form = NutricionistaForm()
    return render(request, 'login/adm/registrar_nutricionista.html', {'form': form})

def logar_adm(request):
    return render(request, 'login/adm/logar_adm.html')


def logout_view(request):
    logout(request)
    return redirect('home')