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





