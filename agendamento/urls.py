from django.urls import path
from . import views

urlpatterns = [
    path('cliente/pagina_inicial', views.pagina_cliente, name='pagina_cliente'),
    path('cliente/minha_conta', views.minha_conta_cliente, name='minha_conta_cliente'),
    path('cliente/agendar_consulta', views.agendar_consulta, name='agendar_consulta'),
    path('nutricionista/pagina_inicial', views.pagina_nutricionista, name='pagina_nutricionista'),
    path('nutricionista/minha_conta_nutricionista', views.minha_conta_nutricionista, name='minha_conta'),
]