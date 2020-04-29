from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm

from .models import Cliente, Productos, Pedido, Componente

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class ProductoForm(ModelForm):
    class Meta:
        model = Productos
        fields = '__all__'

class PedidoForm(ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'

class ComponenteForm(ModelForm):
    class Meta:
        model = Componente
        fields = '__all__'


# Formulario de Registro
class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')


# Formulario de Inicio de Sesion
class LoginForm(forms.Form):
    # Usuario
    username = forms.CharField(max_length=100)

    # Contraseña
    attrs = {
        "type": "password"  # Atributo para mostrarlo como contraseña
    }
    password = forms.CharField(widget=forms.TextInput(attrs=attrs))
