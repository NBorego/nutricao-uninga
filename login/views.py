from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import user_passes_test, login_required
from .forms import ClienteForm, NutricionistaForm, CustomAuthenticationForm

def tipo_login(request):
    return render(request, 'login/tipo_login.html')

def login_cliente(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()

            if user.is_cliente:
                login(request, user)
                return redirect('pagina_cliente')
            
            erro = 'Este e-mail não está cadastrado como cliente. Por favor, faça login como nutricionista.'

            return render(
                request, 
                'login/login_cliente.html', 
                {'form': form, 'erro': erro}
            )
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login/login_cliente.html', {'form': form})
    
def login_nutricionista(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()

            if user.is_nutricionista or user.is_superuser:
                login(request, user)
                return redirect('pagina_nutricionista')
            
            erro = 'Este e-mail não está cadastrado como nutricionista. Por favor, faça login como cliente.'

            return render(
                request, 
                'login/login_cliente.html', 
                {'form': form, 'erro': erro}
            )
    else: 
        form = CustomAuthenticationForm() 
    
    return render(request, 'login/login_nutricionista.html', {'form': form})
    
def registrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST, request.FILES)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('pagina_cliente')
    else:
        form = ClienteForm()
    return render(request, 'login/registrar_cliente.html', {'form': form})

@login_required(login_url='logar_adm')
@user_passes_test(lambda u: u.is_superuser, login_url='logar_adm')
def registrar_nutricionista(request):
    if request.method == 'POST':
        form = NutricionistaForm(request.POST, request.FILES)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('pagina_nutricionista')
    else:
        form = NutricionistaForm()
    return render(request, 'login/adm/registrar_nutricionista.html', {'form': form})

def logar_adm(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)

            if user.is_superuser:
                return redirect('registrar_nutricionista')
    else: 
        form = CustomAuthenticationForm()

    return render(request, 'login/adm/logar_adm.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')