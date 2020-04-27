from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .forms import ClienteForm, ProductoForm
from .models import Pedido, Productos, Cliente, Componente
from django.views.generic import CreateView, DeleteView, DetailView


#PAGINA DE INICIO
def index(request):
    return render(request, 'base.html')

def prueba1(request):
    return render(request, 'Usos.html')

# CLIENTES
# Listado de clientes
def cliente(request):
    clientes = Cliente.objects.order_by('CIF')
    context = {'titulo_form': 'Listado de clientes','titulo_pagina':'Añadir un cliente','lista_clientes': clientes}
    return render(request, 'clientes.html', context)

def cliente_id(request, cliente_id):
    cliente = Productos.objects.get(pk=cliente_id)
    return render(request, 'clientes.html')


class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente_añadir.html'

    def get_success_url(self):
        return reverse('cliente')



#PEDIDOS
# Listado de pedidos
def lista_pedidos(request):
    pedidos = Pedido.objects.order_by('codigo')
    context = {'titulo_form': 'Añadir un pedido','titulo_pagina':'Listado de pedidos','lista_pedidos': pedidos}
    return render(request, 'pedidos.html', context)


def cliente_nombre(request):
    clientes = Cliente.objects.order_by('empresa')
    context = {'lista_clientes': clientes}
    return render(request, 'pedidos.html', context)


def pedido_por_codigo(request, pedido_codigo):
    pedidos = Pedido.objects.get(pk=pedido_codigo)
    context = {'lista_pedidos': pedidos}
    return render(request,'nuevopedido.html', context)


def añadir_pedido(request):
    return render(request, 'nuevopedido.html')



#COMPONENTES
def componente(request, componente_codigo):
    componente = Componente.objects.get(pk=componente_codigo)
    return HttpResponse(componente)


#PRODUCTOS
def lista_productos(request):
    productos = Productos.objects.order_by('referencia')
    context = {'titulo_form':'Listado de productos','lista_productos': productos}
    return render(request, 'productos.html', context)


class ProductosCreateView(CreateView):
    model = Productos
    form_class = ProductoForm
    template_name = 'productoañadir.html'

    def get_success_url(self):
        return reverse('indexprod')


class ProdcutoDetailView(DetailView):
    model = Productos
    template_name = 'producto_detalle.html'

    def get_context_data(self, **kwargs):
        context = super(ProdcutoDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Detalles del proyecto'
        return context








