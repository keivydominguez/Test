from django.db import models


class Tipo(models.Model):
    tipo_nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.tipo_nombre

class Marca(models.Model):
    marca_nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.marca_nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=200, blank=False, null=False)
    tipo   = models.ForeignKey(Tipo, on_delete=models.CASCADE, null=True, blank=True)
    marca  = models.ForeignKey(Marca, on_delete=models.CASCADE, null=True, blank=True)
    precio = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.nombre


class Numero(models.Model):
    numero1 = models.CharField(max_length=100)
    numero2 = models.CharField(max_length=100)
    numero3 = models.CharField(max_length=100)

    def __str__(self):
        return self.numero1