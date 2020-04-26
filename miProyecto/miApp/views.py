from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Pedido, Productos, Cliente, Componente


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

def producto_id(request, producto_id):
    producto = Productos.objects.get(pk=producto_id)
    return render(request, 'productos.html')


def añadir_prod(request):
    return render(request, 'productos_añadir.html')


def mostrar_prod_añadido(request):
    context = {
        'referencia': request.POST("Referencia"),
        'precio': request.POST("Precio"),
        'nombre': request.POST("Nombre"),
        'descripcion': request.POST("Descripcion"),
        'categoria': request.POST("Categoria"),
        'tipo_componentes': request.POST("Tipo_componentes")
    }
    Productos.object.add(context)






