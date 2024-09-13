from django.urls import path
from . import views

urlpatterns = [
    path('cliente/pagina_inicial/', views.pagina_cliente, name='pagina_cliente'),
    path('cliente/minhas_consultas/', views.minhas_consultas, name='minhas_consultas'),
    path('cliente/agendar_consulta/', views.agendar_consulta, name='agendar_consulta'),
    path('nutricionista/pagina_inicial/', views.pagina_nutricionista, name='pagina_nutricionista'),
    path('nutricionista/minha_agenda/', views.minha_agenda, name='minha_agenda'),
    path('nutricionista/aceitar/<int:consulta_id>/', views.aceitar_consulta, name='aceitar_consulta'),
    path('nutricionista/cancelar/<int:consulta_id>/', views.cancelar_consulta, name='cancelar_consulta'),
    path('nutricionista/editar_consulta/<int:consulta_id>/', views.editar_consulta, name='editar_consulta'),
    path('minha_conta_nutricionista/', views.minha_conta, name='minha_conta'),
    path('mudar_foto/<int:usuario_id>/', views.mudar_foto, name='mudar_foto'),
    path('mudar_senha/', views.mudar_senha, name='mudar_senha'),
    path('excluir_conta/', views.excluir_conta, name='excluir_conta'),
]