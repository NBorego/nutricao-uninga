from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .forms import AlimentoForm
from .models import Alimento

def home(request):
    alimentos = Alimento.objects.all().order_by('nome')[:4]

    return render(request, 'home.html', {'alimentos': alimentos})

def catalogo(request):
    # Filtragem
    obj = request.GET.get('obj')

    if obj:
        alimentos = Alimento.objects.filter(nome__icontains=obj).order_by('nome')
    else:        
        alimentos = Alimento.objects.all().order_by('nome')

    # Paginação
    alimentos_paginador = Paginator(alimentos, 12)  
    num_pagina = request.GET.get('page')
    pagina = alimentos_paginador.get_page(num_pagina)
    pagina.adjusted_elided_pages = alimentos_paginador.get_elided_page_range(num_pagina)

    return render(request, 'catalogo/catalogo.html', {'pagina': pagina})

def alimento(request, id):
    alimento = Alimento.objects.get(id = id)
    return render(request, 'catalogo/alimento.html', {'alimento': alimento})


def add(request):
    if request.method == 'POST':
        form = AlimentoForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('catalogo')
    else:
        form = AlimentoForm()
    return render(request, 'catalogo/add.html', {'form': form})