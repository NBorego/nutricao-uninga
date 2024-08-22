from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Cliente, Nutricionista

class ClienteForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'password1', 'password2']

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
