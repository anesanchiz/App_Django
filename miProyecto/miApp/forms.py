from django.forms import ModelForm
from .models import Cliente, Productos

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class ProductoForm(ModelForm):
    class Meta:
        model = Productos
        fields = '__all__'