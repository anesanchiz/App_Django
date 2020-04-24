from django.urls import path
from . import views


urlpatterns = [

     #URLS QUE FUNCIONAN
     path('', views.index, name='index'),
     path('productos/', views.productos, name='indexprod'),
     path('productos/añadir', views.añadir_prod, name='productos'),
     path('pedidos', views.pedidos, name='pedidos'),
     path('clientes/', views.cliente, name='cliente'),

     #URLS QUE NO FUNCIONAN
     path('productos/productos/<producto_id>', views.producto, name='producto'),
     path('clientes/<int:cliente_CIF>/', views.cliente, name='cliente'),
     path('componenete/<int:componente_codigo>/', views.componente, name='detail'),
     path('productos/<int:productos_referencia>/', views.productos, name='detail'),
     path('pedido/<int:pedido_codigo>/', views.pedido, name='detail')

]
