from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

#Devuelve el listado de clientes
from .models import Pedido, Productos, Cliente, Componente

def index(request):
    clientes = Cliente.objects.order_by('empresa')
    output = ', '.join([d.empresa for d in clientes])
    return HttpResponse(output)

#Devuelve los datos del cliente
def detail(request, cliente_id):
    clientes = Cliente.objects.get(pk=cliente_id)
    return HttpResponse(clientes)
