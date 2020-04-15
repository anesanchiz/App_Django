from django.contrib import admin
from .models import Pedido, Productos, Cliente, Componente

admin.site.register(Pedido)
admin.site.register(Productos)
admin.site.register(Cliente)
admin.site.register(Componente)
