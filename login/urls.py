from django.urls import path
from . import views

urlpatterns = [
    path('tipo_login', views.tipo_login, name='tipo_login'),
    path('login_cliente', views.login_cliente, name='login_cliente'),
    path('login_nutricionista', views.login_nutricionista, name='login_nutricionista'),
    path('registrar_cliente', views.registrar_cliente, name="registrar_cliente"),
    path('adm', views.logar_adm, name="logar_adm"),
    path('adm/registrar_nutricionista', views.registrar_nutricionista, name="registrar_nutricionista")
]