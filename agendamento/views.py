from django.contrib.auth.decorators import permission_required, login_required
from django.shortcuts import render, redirect
from .models import Agendamento
from .forms import AgendamentoForm

@login_required
@permission_required('login.cliente')
def pagina_cliente(request):
    agendamentos = Agendamento.objects.all().order_by('dia') 

    return render(request, 
        'agendamento/cliente/pagina_inicial.html', {'agendamentos': agendamentos}
    )

@login_required
@permission_required('login.cliente')
def agendar_consulta(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('pagina_cliente')
    else:
        form = AgendamentoForm()
    return render(request, 'agendamento/cliente/agendar_consulta.html', {'form': form})

@login_required
@permission_required('login.cliente')
def minha_conta_cliente(request): 
    return render(request, 'agendamento/cliente/minha_conta.html')

@login_required
@permission_required('login.nutricionista')
def pagina_nutricionista(request):
    return render(request, 'agendamento/nutricionista/pagina_inicial.html')

@login_required
@permission_required('login.nutricionista')
def minha_conta_nutricionista(request): 
    return render(request, 'agendamento/nutricionista/minha_conta.html')

