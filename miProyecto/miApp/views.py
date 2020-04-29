from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse,reverse_lazy
from django.contrib.auth.models import User
from .forms import ClienteForm, ProductoForm, PedidoForm, ComponenteForm, RegisterForm, LoginForm
from .models import Pedido, Productos, Cliente, Componente
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView


#PAGINA DE INICIO
def index(request):
    return render(request, 'base.html')

def prueba1(request):
    return render(request, 'Usos.html')


# Sesiones
# -Pagina de login
def get_login(req):
    context = {'form': RegisterForm, 'login': LoginForm}
    return render(req, "login.html", context)


# -Funcion para hacer el login
def do_login(req):
    print('lego aqui')
    username = req.POST['username']
    password = req.POST['password']
    user = authenticate(req, username=username, password=password)
    if user is not None:
        login(req, user)
        print('bien')
        print(req.GET)
        return redirect('index')
    else:
        print('mal')
        return redirect('get_login')


# -Funcion para hacer el logout
def do_logout(req):
    logout(req)
    return redirect('get_login')


# -Funcion para hacer el registro
def register(req):
    form = RegisterForm(req.POST)
    if (form.is_valid):
        form.save()
        # user=authenticate(req,username=form.cleaned_data['username'],password=form.cleaned_data['password'])
        # if user is not None:
        #     login(req, user)
        print("valido")
        return redirect('index')
    else:
        print("no valido")
        return redirect('get_login')

# CLIENTES
# Listado de clientes
def cliente(request):
    clientes = Cliente.objects.order_by('CIF')
    context = {'titulo_form': 'Listado de clientes','titulo_pagina':'Añadir un cliente','lista_clientes': clientes}
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
    model = Cliente
    template_name = 'cliente_eliminar.html'
    success_url = reverse_lazy('cliente')

    def get_context_data(self, **kwargs):
        context = super(ClienteDelete, self).get_context_data(**kwargs)
        return context

#Actualizar
class ClienteUpdate(UpdateView):
    model = Cliente
    fields = ['empresa','telefono']
    template_name = 'añadir.html'
    success_url = reverse_lazy('cliente')


#PEDIDOS
# Listado de pedidos
def lista_pedidos(request):
    pedidos = Pedido.objects.order_by('codigo')
    context = {'titulo_form': 'Añadir un pedido','titulo_pagina':'Listado de pedidos','lista_pedidos': pedidos}
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
    context = {'titulo_form': 'Añadir un componente','titulo_pagina':'Listado de componentes','lista_componente': componente}
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
#Listado de prductos
def lista_productos(request):
    productos = Productos.objects.order_by('referencia')
    context = {'titulo_form':'Listado de productos','lista_productos': productos}
    return render(request, 'productos.html', context)

#Añadir
class ProductosCreateView(CreateView):
    model = Productos
    form_class = ProductoForm
    template_name = 'añadir.html'

    def get_success_url(self):
        return reverse('indexprod')

#Detalles
class ProdcutoDetailView(DetailView):
    model = Productos
    template_name = 'producto_detalle.html'

    def get_context_data(self, **kwargs):
        context = super(ProdcutoDetailView, self).get_context_data(**kwargs)
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

