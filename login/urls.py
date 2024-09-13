from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('tipo_login', views.tipo_login, name='tipo_login'),
    path('login_cliente', views.login_cliente, name='login_cliente'),
    path('login_nutricionista', views.login_nutricionista, name='login_nutricionista'),
    path('registrar_cliente', views.registrar_cliente, name="registrar_cliente"),
    path('adm/registrar_nutricionista', views.registrar_nutricionista, name="registrar_nutricionista"),
    path('logout/', views.logout_view, name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]