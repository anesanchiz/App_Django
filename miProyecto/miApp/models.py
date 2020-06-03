from django.db import models


class Factura(models.Model):
    imagen = models.ImageField(upload_to="facturas", blank=True)
    fecha = models.DateField()


class Cliente(models.Model):
    CIF = models.CharField(max_length=9)
    empresa = models.CharField(max_length=30)
    telefono = models.IntegerField()

    def __str__(self):
        return f"Empresa: {self.empresa}"


class Componente(models.Model):
    codigo = models.CharField(max_length=20, default='')
    modelo = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)

    def __str__(self):
        return f"Codigo: {self.codigo}, Modelo: {self.modelo}, Marca: {self.marca}"


class Productos(models.Model):
    referencia = models.CharField(max_length=50)
    precio = models.IntegerField()
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)
    categoria = models.CharField(max_length=40)  # DICCIONARIO DE CATEGORIAS(?
    tipo_componentes = models.ManyToManyField(Componente)

    def __str__(self):
        return f"Ref: {self.referencia}; Nombre: {self.nombre}; Precio: {self.precio}"


class Pedido(models.Model):
    codigo = models.CharField(max_length=20)
    fecha = models.DateField()
    datos_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Productos)
    cantidad = models.IntegerField()
    precio_total = models.IntegerField()

    def __str__(self):
        return f"Cod: {self.codigo}, Cliente: {self.datos_cliente}, Product: {self.productos}, Uds: {self.cantidad}, Precio: {self.precio_total}"
