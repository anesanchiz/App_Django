from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse,reverse_lazy
from django.contrib.auth.models import User
from .forms import ClienteForm, ProductoForm, PedidoForm, ComponenteForm, RegisterForm, LoginForm
from .models import Pedido, Productos, Cliente, Componente
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from django.http import JsonResponse
from django.forms import model_to_dict
from django.views import View

#VIEWS JS

class PedidoListView_js(View):
    def get(self, request):
        if ('name' in request.GET):
           pedido_list = Pedido.objects.filter(name_contains=request.GET['name'])
        else:
            pedido_list = Pedido.objects.all()
        return JsonResponse(list(pedido_list.values()), safe=False)


class PedidoDetailView_js(View):
    def get(self, request, pk):
        pedido = Pedido.objects.get(pk=pk)
        return JsonResponse(model_to_dict(pedido))




#PAGINA DE INICIO
def index(request):
    context = {'titulo_form': 'Menu Principal'}
    return render(request, 'base.html')

def prueba1(request):
    return render(request, 'Usos.html')



# CLIENTES
# Listado de clientes
def cliente(request):
    clientes = Cliente.objects.order_by('CIF')
    context = {'titulo_form': 'Listado de clientes','titulo_pagina':'Clientes','lista_clientes': clientes}
    return render(request, 'clientes.html', context)

#Añadir
class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'añadir.html'

    def get_success_url(self):
        return reverse('cliente')

#Eliminar
class ClienteDelete(DeleteView):
    model = Cliente #modelo que se esta utilizando
    template_name = 'cliente_eliminar.html' #template que se va a utilizar
    success_url = reverse_lazy('cliente') #template a la que va a volver

    def get_context_data(self, **kwargs):
        context = super(ClienteDelete, self).get_context_data(**kwargs)
        return context

#Actualizar
class ClienteUpdate(UpdateView):
    model = Cliente
    fields = ['CIF','empresa','telefono']
    template_name = 'añadir.html'
    success_url = reverse_lazy('cliente')




#PEDIDOS
# Listado de pedidos
def lista_pedidos(request):
    pedidos = Pedido.objects.order_by('codigo')
    context = {'titulo_form': 'Listado de pedidos','titulo_pagina':'Pedidos','lista_pedidos': pedidos}
    return render(request, 'pedidos.html', context)

#Añadir
class PedidoCreateView(CreateView):
    model = Pedido
    form_class = PedidoForm
    template_name = 'añadir.html'

    def get_success_url(self):
        return reverse('pedidos')


#Detalles
class PedidoDetailView(DetailView):
    model = Pedido
    template_name = 'pedido_detalle.html'

    def get_context_data(self, **kwargs):
        context = super(PedidoDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Detalles del pedido'
        return context


#Eliminar
class PedidoDelete(DeleteView):
    model = Pedido
    template_name = 'pedido_eliminar.html'
    success_url = reverse_lazy('pedidos')

    def get_context_data(self, **kwargs):
        context = super(PedidoDelete, self).get_context_data(**kwargs)
        return context

#Actualizar
class PedidoUpdate(UpdateView):
    model = Pedido
    fields = ['datos_cliente','productos','cantidad','precio_total']
    template_name = 'añadir.html'
    success_url = reverse_lazy('pedidos')


#COMPONENTES
#Listado de Componentes
def lista_componente(request):
    componente = Componente.objects.order_by('codigo')
    context = {'titulo_form': 'Listado de componentes','titulo_pagina':'Componentes','lista_componente': componente}
    return render(request, 'componentes.html', context)

#Añadir
class ComponenteCreateView(CreateView):
    model = Componente
    form_class = ComponenteForm
    template_name = 'añadir.html'

    def get_success_url(self):
        return reverse('componentes')

#Detalles
class ComponenteDetailView(DetailView):
    model = Componente
    template_name = 'componente_detalle.html'

    def get_context_data(self, **kwargs):
        context = super(ComponenteDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Detalles del componente'
        return context

#Eliminar
class ComponenteDelete(DeleteView):
    model = Componente
    template_name = 'componente_eliminar.html'
    success_url = reverse_lazy('componentes')

    def get_context_data(self, **kwargs):
        context = super(ComponenteDelete, self).get_context_data(**kwargs)
        return context

#Actualizar
class ComponenteUpdate(UpdateView):
    model = Componente
    fields = ['codigo','modelo','marca']
    template_name = 'añadir.html'
    success_url = reverse_lazy('componentes')


#PRODUCTOS
#Listado de productos
def lista_productos(request):
    productos = Productos.objects.order_by('referencia')
    context = {'titulo_form':'Listado de productos','titulo_pagina':'Productos' ,'lista_productos': productos}
    return render(request, 'productos.html', context)

#Añadir
class ProductosCreateView(CreateView):
    model = Productos
    form_class = ProductoForm
    template_name = 'añadir_producto.html'

    def get_success_url(self):
        return reverse('indexprod')


#Detalles
class ProductoDetailView(DetailView):
    model = Productos
    template_name = 'producto_detalle.html'

    def get_context_data(self, **kwargs):
        context = super(ProductoDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Detalles del producto'
        return context

#Eliminar
class ProductoDelete(DeleteView):
    model = Productos
    template_name = 'producto_eliminar.html'
    success_url = reverse_lazy('indexprod')

    def get_context_data(self, **kwargs):
        context = super(ProductoDelete, self).get_context_data(**kwargs)
        return context

#Actualizar
class ProductoUpdate(UpdateView):
    model = Productos
    fields = ['referencia','precio','nombre','descripcion','categoria', 'tipo_componentes']
    template_name = 'añadir.html'
    success_url = reverse_lazy('indexprod')





