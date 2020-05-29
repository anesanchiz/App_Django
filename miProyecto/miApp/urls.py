from django.urls import path
from . import views


urlpatterns = [
     path('', views.index, name='index'),


     #AÑADIDAS
     path('facturas/', views.FacturasView, name= 'facturas'),
     path('pedidosjs/', views.PedidoListView_js.as_view(), name = 'pedidosjs'),
     path('success/', views.success, name='success'),

     path('productos/', views.lista_productos, name='indexprod'),
     path('productos/order-nombre/', views.lista_productos1, name='prod_order_1'),
     path('productos/order-precio/', views.lista_productos2, name='prod_order_2'),

     path('productonuevo/', views.ProductosCreateView.as_view(), name='productonuevo'),
     path('productoeditar/<int:pk>/', views.ProductoUpdate.as_view(), name='productoeditar'),
     path('productoeliminar/<int:pk>/', views.ProductoDelete.as_view(), name='productoeliminar'),
     path('productos/<int:pk>/', views.ProductoDetailView.as_view(), name='productodetalle'),


     path('pedidos/', views.lista_pedidos, name='pedidos'),
     path('pedidonuevo/', views.PedidoCreateView.as_view(), name='pedidonuevo'),
     path('pedidoeditar/<int:pk>/', views.PedidoUpdate.as_view(), name='pedidoeditar'),
     path('pedidoeliminar/<int:pk>/', views.PedidoDelete.as_view(), name='pedidoeliminar'),
     path('pedidos/<int:pk>/', views.PedidoDetailView.as_view(), name='pedidodetalle'),


     path('clientes/', views.cliente, name='cliente'),
     path('clientenuevo/', views.ClienteCreateView.as_view(), name='cliente_nuevo'),
     path('clienteeditar/<int:pk>/', views.ClienteUpdate.as_view(), name='clienteeditar'),
     path('clienteeliminar/<int:pk>/', views.ClienteDelete.as_view(), name='cliente_eliminar'),

     path('componentes/', views.lista_componente, name='componentes'),
     path('componentenuevo/', views.ComponenteCreateView.as_view(), name='componentenuevo'),
     path('componenteeditar/<int:pk>/', views.ComponenteUpdate.as_view(), name='componenteeditar'),
     path('componenteeliminar/<int:pk>/', views.ComponenteDelete.as_view(), name='componenteeliminar'),
     path('componentes/<int:pk>/', views.ComponenteDetailView.as_view(), name='componentedetalle'),
]
