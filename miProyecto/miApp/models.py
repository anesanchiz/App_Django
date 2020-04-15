from django.db import models

class Cliente (models.Model):
    CIF = models.CharField(max_length=9)
    empresa = models.CharField(max_length=30)
    telefono = models.IntegerField()

    def __str__(self):
        return f"CIF={self.CIF}, empresa={self.empresa}, telefono={self.telefono}"


class Componente(models.Model):
    codigo = models.CharField(max_length=10)
    modelo = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)

    def __str__(self):
        return f"codigo={self.codigo}, nombre={self.modelo}, marca={self.marca}"



class Productos(models.Model):
    referencia = models.CharField(max_length=50)
    precio = models.IntegerField
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)
    categoria = models.CharField(max_length=40) #DICCIONARIO DE CATEGORIAS(?
    tipo_componentes = models.ManyToManyField(Componente)

    def __str__(self):
        return f"referncia={self.nombre}, precio={self.precio}," \
               f" nombre={self.nombre}, descripcion={self.descripcion}, " \
               f"categoria={self.categoria}, componentes={self.tipo_componentes}"



class Pedido(models.Model):
    codigo = models.CharField #PRIMARY KEY (?)
    fecha = models.DateField()
    datos_cliente = models.ForeignKey(Cliente, on_delete= models.CASCADE)
    productos = models.ManyToManyField(Productos)
    cantidad = models.IntegerField
    precio_total = models.IntegerField

    def __str__(self):
        return f"codigo={self.codigo}, fecha={self.fecha}, datos cliente={self.datos_cliente}" \
               f", productos={self.productos}, cantidad={self.cantidad}, precio={self.precio_total}"
