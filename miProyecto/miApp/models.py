from django.db import models

class Cliente (models.Model):
    CIF = models.CharField(max_length=9)
    empresa = models.CharField(max_length=30)
    telefono = models.IntegerField()


class Componente(models.Model):
    codigo = models.CharField(max_length=10)
    modelo = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)


class Productos(models.Model):
    referencia = models.CharField(max_length=50)
    precio = models.IntegerField
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)
    categoria = models.CharField(max_length=40) #DICCIONARIO DE CATEGORIAS(?
    tipo_componentes = models.ManyToManyField(Componente)


class Pedido(models.Model):
    codigo = models.CharField #PRIMARY KEY (?)
    fecha = models.DateField()
    datos_cliente = models.ForeignKey(Cliente, on_delete= models.CASCADE)
    productos = models.ManyToManyField(Productos)
    cantidad = models.IntegerField
    precio_total = models.IntegerField
