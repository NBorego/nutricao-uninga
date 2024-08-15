from django.shortcuts import render

def pagina_cliente(request):
    return render(request, 'agendamento/cliente/pagina_inicial.html')

def agendar_consulta(request):
    return render(request, 'agendamento/cliente/agendar_consulta.html')

def minha_conta_cliente(request): 
    return render(request, 'agendamento/cliente/minha_conta.html')
    
def pagina_nutricionista(request):
    return render(request, 'agendamento/nutricionista/pagina_inicial.html')

def minha_conta_nutricionista(request): 
    return render(request, 'agendamento/nutricionista/minha_conta.html')

