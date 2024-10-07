from django.db import models
from clientes.models import Cliente

# Create your models here.

class MarcaMotor(models.Model):
    descripcion = models.CharField(max_length=100)
    usuario = models.CharField(max_length=100, null=True)


    def __str__(self):
        return self.descripcion

class MarcaGenerador(models.Model):
    descripcion = models.CharField(max_length=100)
    usuario = models.CharField(max_length=100, null=True)


    def __str__(self):
        return self.descripcion

class MarcaModulo(models.Model):
    descripcion = models.CharField(max_length=100)
    usuario = models.CharField(max_length=100, null=True)


    def __str__(self):
        return self.descripcion

class MarcaControlador(models.Model):
    descripcion = models.CharField(max_length=100)
    usuario = models.CharField(max_length=100, null=True)


    def __str__(self):
        return self.descripcion

class Uso(models.Model):
    descripcion = models.CharField(max_length=100)
    usuario = models.CharField(max_length=100, null=True)


    def __str__(self):
        return self.descripcion

class Equipo(models.Model):
    descripcion = models.CharField(max_length=100)
    observaciones = models.CharField(blank=True)
    Horometro = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)  # Campo para latitud
    longitude = models.FloatField(null=True, blank=True)  # Campo para longitud
    Potencia = models.FloatField(null=True, blank=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    uso = models.ForeignKey(Uso, on_delete=models.PROTECT)
    marcamotor = models.ForeignKey(MarcaMotor, on_delete=models.PROTECT)
    marcagenerador = models.ForeignKey(MarcaGenerador, on_delete=models.PROTECT)
    marcamodulo = models.ForeignKey(MarcaModulo, on_delete=models.PROTECT)
    marcacontrolador = models.ForeignKey(MarcaControlador, on_delete=models.PROTECT)
    usuario = models.CharField(max_length=100, null=True)


    def __str__(self):
        return self.descripcion