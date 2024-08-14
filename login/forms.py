from django import forms
from .models import Nutricionista, Cliente

class NutricionistaLoginForm(forms.ModelForm):
    ra = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control mb-2'}
    ))
    senha = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control mb-2'}
    ))

    class Meta:
        model = Nutricionista
        fields = ('ra', 'senha')


class ClienteLoginForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control mb-4'}
    ))
    senha = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control mb-4'}
    ))

    class Meta:
        model = Cliente
        fields = ('email', 'senha')

class RegistrarClienteForm(forms.ModelForm):
    usuario = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control mb-4'}
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control mb-4'}
    ))
    senha = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control mb-4'}
    ))

    class Meta:
        model = Cliente
        fields = ('usuario', 'email', 'senha')

class RegistrarNutricionistaForm(forms.ModelForm):
    usuario = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control mb-2'}
    ))
    foto = forms.ImageField(widget=forms.FileInput(
        attrs={'class': 'form-control mb-2'}
    ))
    ra = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control mb-2'}
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control mb-2'}
    ))
    senha = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control mb-2'}
    ))


    class Meta:
        model = Nutricionista
        fields = ('usuario','foto', 'email', 'ra', 'senha')