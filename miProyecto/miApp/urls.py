from django.urls import path
from . import views


urlpatterns = [

     #URLS QUE FUNCIONAN
     path('', views.index, name='index'),

     path('productos/', views.lista_productos, name='indexprod'),
     path('productos/añadir/', views.añadir_prod, name='productos'),
     path('productos/productos/<producto_id>', views.producto, name='producto'),
     path('prueba1',views.prueba1, name = 'prueba'),

     path('pedidos/', views.lista_pedidos, name='pedidos'),
     path('pedidos/cli_exist/', views.añadir_pedido, name='newpedido'),

     path('clientes/', views.cliente, name='cliente'),


     #URLS QUE NO FUNCIONAN

     path('clientes/<int:cliente_CIF>/', views.cliente, name='cliente'),
     path('componenete/<int:componente_codigo>/', views.componente, name='detail'),
     path('productos/<int:productos_referencia>/', views.lista_productos, name='detail'),
     path('pedido/<int:pedido_codigo>/', views.pedido_por_codigo, name='detail')

]
