from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, Cliente, Nutricionista

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label=_("Email"),
        max_length=254,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        })
    )
    password = forms.CharField(
        label=_("Senha"),
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
        }),
    )

    error_messages = {
        "invalid_login": _(
            "O %(username)s ou a senha está incorreto."
        ),
        "inactive": _("Esta conta está inativa."),
    }

class ClienteForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = [
            'email',
            'password1', 
            'password2'
        ]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_cliente = True

        if commit:
            user.save()
            Cliente.objects.create(user=user)
        return user

class NutricionistaForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_nutricionista = True

        if commit:
            user.save()
            Nutricionista.objects.create(user=user)
        return user
