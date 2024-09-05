from django.contrib.auth.decorators import permission_required, login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Agendamento
from .forms import AgendamentoForm
from login.models import Cliente

# Cliente
@login_required
@permission_required('login.cliente')
def pagina_cliente(request):
    consultas = Agendamento.objects.filter(cliente=request.user.cliente).order_by('dia') 

    return render(request, 
        'agendamento/cliente/pagina_inicial.html', {'consultas': consultas}
    )

@login_required
@permission_required('login.cliente')
def minhas_consultas(request):
    status_filtro = request.GET.get('status')  
    
    if status_filtro:
        consultas = Agendamento.objects.filter(
            status=status_filtro,
            cliente=request.user.cliente
        )
    else:
        consultas = Agendamento.objects.filter(
            cliente=request.user.cliente
        ).order_by('dia') 

    return render(
        request, 
        'agendamento/cliente/minhas_consultas.html',
        {'consultas': consultas}
    )

@login_required
@permission_required('login.cliente')
def agendar_consulta(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST, cliente=request.user.cliente)

        if form.is_valid():
            form.save()
            return redirect('pagina_cliente')
    else:
        form = AgendamentoForm(cliente=request.user.cliente)
    return render(request, 'agendamento/cliente/agendar_consulta.html', {'form': form})

@login_required
@permission_required('login.cliente')
def minha_conta_cliente(request): 
    return render(request, 'agendamento/cliente/minha_conta.html')

# Nutricionista
@login_required
@permission_required('login.nutricionista')
def pagina_nutricionista(request):
    return render(
        request, 
        'agendamento/nutricionista/pagina_inicial.html', 
    )

@login_required
@permission_required('login.nutricionista')
def minha_agenda(request):
    status_filtro = request.GET.get('status')  
    
    if status_filtro:
        consultas = Agendamento.objects.filter(
            status=status_filtro,
            nutricionista=request.user.nutricionista
        )
    else:
        consultas = Agendamento.objects.filter(
            nutricionista=request.user.nutricionista
        ).order_by('dia') 

    return render(
        request, 
        'agendamento/nutricionista/minha_agenda.html',
        {'consultas': consultas}
    )

@login_required
@permission_required('login.nutricionista')
def aceitar_consulta(request, consulta_id):
    consulta = get_object_or_404(Agendamento, id=consulta_id)
    consulta.status = 'Confirmado'
    consulta.save()
    return redirect('minha_agenda')  

@login_required
def cancelar_consulta(request, consulta_id):
    consulta = get_object_or_404(Agendamento, id=consulta_id)
    consulta.delete()

    if request.user.is_nutricionista:
        return redirect('minha_agenda')
    else:
        return redirect('pagina_cliente')

@login_required
@permission_required('login.nutricionista')
def minha_conta_nutricionista(request): 
    return render(request, 'agendamento/nutricionista/minha_conta.html')

