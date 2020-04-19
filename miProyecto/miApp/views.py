from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Pedido, Productos, Cliente, Componente

#CLIENTES

#Devuelve los clientes ordenados por orden alf
#def index(request):
#    clientes = Cliente.objects.order_by('empresa')
#    output = ', '.join([d.empresa for d in clientes])
#    return HttpResponse(output)

def index(request):
    clientes = Cliente.objects.order_by('empresa')
    context = {'lista_clientes' : clientes}
    return render(request, 'prueba.html', context)

#Devuelve los datos del cliente dado
def detail(request, cliente_id):
    clientes = Cliente.objects.get(pk=cliente_id)
    return HttpResponse(clientes)



