from django.urls import path
from . import views

urlpatterns = [
     path('', views.index, name='index'),
     path('clientes/<int:cliente_CIF>/', views.cliente, name='detail'),
     path('componenete/<int:componente_codigo>/', views.componente, name='detail'),
     path('productos/<int:productos_referencia>/', views.productos, name='detail'),
     path('pedido/<int:pedido_codigo>/', views.pedido, name='detail')

]
