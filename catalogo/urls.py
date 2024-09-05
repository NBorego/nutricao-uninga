from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('catalogo/<int:id>/', views.alimento, name='alimento'),
    path('catalogo/adicionar_alimento/', views.adicionar_alimento, name='adicionar_alimento')
]