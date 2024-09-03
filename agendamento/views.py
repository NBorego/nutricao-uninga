from django.contrib.auth.decorators import permission_required, login_required
from django.shortcuts import render
from .models import Agendamento

@login_required
@permission_required('login.cliente')
def pagina_cliente(request):
    agendamentos = Agendamento.objects.all().order_by('nome') 

    return render(request, 
        'agendamento/cliente/pagina_inicial.html', {'agendamentos': agendamentos}
    )

@login_required
@permission_required('login.cliente')
def agendar_consulta(request):
    return render(request, 'agendamento/cliente/agendar_consulta.html')

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

