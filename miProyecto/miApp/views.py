from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Pedido, Productos, Cliente, Componente


# CLIENTES

# Devuelve los clientes ordenados por orden alf
# def index(request):
#    clientes = Cliente.objects.order_by('empresa')
#    output = ', '.join([d.empresa for d in clientes])
#    return HttpResponse(output)


# Pagina de inicio
def index(request):
    clientes = Cliente.objects.order_by('empresa')
    context = {'lista_clientes': clientes}
    return render(request, 'base.html', context)


# Devuelve los datos del cliente dado
def cliente(request):
    clientes = Cliente.objects.order_by('CIF')
    context = {'lista_clientes': clientes}
    return render(request, 'clientes.html', context)


def cliente_nombre(request):
    clientes = Cliente.objects.order_by('empresa')
    context = {'lista_clientes': clientes}
    return render(request, 'pedidos.html', context)


# Listado de pedidos ordenado por codigo
def lista_pedidos(request):
    pedidos = Pedido.objects.order_by('codigo')
    context = {'lista_pedidos': pedidos}
    return render(request, 'pedidos.html', context)

def pedido_por_codigo(request, pedido_codigo):
    pedidos = Pedido.objects.get(pk=pedido_codigo)
    context = {'lista_pedidos': pedidos}
    return render(request,'nuevopedido.html', context)

def añadir_pedido(request):
    return render(request, 'nuevopedido.html')

def componente(request, componente_codigo):
    componente = Componente.objects.get(pk=componente_codigo)
    return HttpResponse(componente)


def lista_productos(request):
    productos = Productos.objects.order_by('referencia')
    context = {'lista_productos': productos}
    return render(request, 'productos.html', context)


def producto(request, producto_id):
    producto = Productos.objects.get(pk=producto_id)
    return HttpResponse(producto)


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



