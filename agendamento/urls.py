from django.urls import path
from . import views

urlpatterns = [
    path('cliente/pagina_inicial', views.pagina_cliente, name='pagina_cliente'),
    path('cliente/minhas_consultas', views.minhas_consultas, name='minhas_consultas'),
    path('cliente/agendar_consulta', views.agendar_consulta, name='agendar_consulta'),
    path('cliente/minha_conta', views.minha_conta_cliente, name='minha_conta_cliente'),
    path('nutricionista/pagina_inicial', views.pagina_nutricionista, name='pagina_nutricionista'),
    path('nutricionista/minha_agenda', views.minha_agenda, name='minha_agenda'),
    path('nutricionista/aceitar/<int:consulta_id>/', views.aceitar_consulta, name='aceitar_consulta'),
    path('nutricionista/cancelar/<int:consulta_id>/', views.cancelar_consulta, name='cancelar_consulta'),
    path('nutricionista/minha_conta_nutricionista', views.minha_conta_nutricionista, name='minha_conta_nutricionita'),
]