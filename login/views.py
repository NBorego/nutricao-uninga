from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from .forms import ClienteForm, NutricionistaForm

# Create your views here.
def tipo_login(request):
    return render(request, 'login/tipo_login.html')

def login_cliente(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)

            if user.is_cliente:
                return redirect('pagina_cliente')
            else:
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login/login_cliente.html', {'form': form})
    
def login_nutricionista(request):
    # if request.method == 'POST':
    #     form = Nu(request.POST)

    #     if form.is_valid():
    #         form.save()
    #         return redirect('login_nutricionista')
    # else: 
    #     form = NutricionistaLoginForm()
        return render(request, 'login/login_nutricionista.html')
    
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
    return render(request, 'login/registrar_nutricionista.html', {'form': form})

def logar_adm(request):
    return render(request, 'login/adm/logar_adm.html')
