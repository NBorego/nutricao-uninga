from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, Cliente, Nutricionista
from django.contrib.auth.models import Permission

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

class ClienteForm(UserCreationForm):
    first_name = forms.CharField(label=_("Nome"))
    last_name = forms.CharField(label=_("Sobrenome"))
    data_nascimento = forms.DateField(
        label=_("Data de nascimento"),
        widget=forms.DateTimeInput(attrs={'type': 'date'}),
    )
    password1 = forms.CharField(
        label=_("Senha"),
        widget=forms.PasswordInput()
    )
    password2 = forms.CharField(
        label=_("Confirmar senha"),
        widget=forms.PasswordInput()
    )

    usable_password = None
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'foto',
            'data_nascimento',
            'password1',
            'password2',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control mb-2'})

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_cliente = True

        if commit:
            user.save()
            permission = Permission.objects.get(codename='cliente', content_type__app_label='login')
            user.user_permissions.add(permission)
            Cliente.objects.create(user=user)
        return user

class NutricionistaForm(UserCreationForm):
    first_name = forms.CharField(label=_("Nome"))
    last_name = forms.CharField(label=_("Sobrenome"))
    data_nascimento = forms.DateField(
        label=_("Data de nascimento"),
        widget=forms.DateTimeInput(attrs={'type': 'date'}),
    )
    password1 = forms.CharField(
        label=_("Senha"),
        widget=forms.PasswordInput()
    )
    password2 = forms.CharField(
        label=_("Confirmar senha"),
        widget=forms.PasswordInput()
    )

    usable_password = None
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'foto',
            'data_nascimento',
            'password1',
            'password2',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control mb-2'})

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_nutricionista = True

        if commit:
            user.save()
            permission = Permission.objects.get(codename='nutricionista', content_type__app_label='login')
            user.user_permissions.add(permission)
            Nutricionista.objects.create(user=user)
        return user
