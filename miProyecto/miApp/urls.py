from django.urls import path
from . import views


urlpatterns = [

     #URLS QUE FUNCIONAN
     path('', views.index, name='index'),

     path('productos/', views.lista_productos, name='indexprod'),
     path('productonuevo/', views.ProductosCreateView.as_view(), name='productonuevo'),
     path('productoeliminar/', views.ProductoDelete.as_view(), name='productoeliminar'),
     path('productos/<int:pk>/', views.ProdcutoDetailView.as_view(), name='productiño'),

     path('pedidos/', views.lista_pedidos, name='pedidos'),
     path('pedidos/cli_exist/', views.añadir_pedido, name='newpedido'),

     path('clientenuevo/', views.ClienteCreateView.as_view(), name = 'cliente_nuevo'),
     path('clientes/', views.cliente, name='cliente'),

     #URLS QUE NO FUNCIONAN


     path('componenete/<int:componente_codigo>/', views.componente, name='detail'),
     path('productos/<int:productos_referencia>/', views.lista_productos, name='detail'),
     path('pedido/<int:pedido_codigo>/', views.pedido_por_codigo, name='detail')

]
