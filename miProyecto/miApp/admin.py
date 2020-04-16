from django.contrib import admin
from .models import Componente, Cliente, Productos, Pedido

admin.site.register(Pedido)
admin.site.register(Productos)
admin.site.register(Cliente)
admin.site.register(Componente)

