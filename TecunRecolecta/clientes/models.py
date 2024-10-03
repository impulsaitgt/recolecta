from django.db import models

# Create your models here.
class Cliente(models.Model):
    cli_id = models.CharField(max_length=100)
    nombre_completo = models.CharField()
    ubicacion = models.CharField()
    latitude = models.FloatField(null=True, blank=True)  # Campo para latitud
    longitude = models.FloatField(null=True, blank=True)  # Campo para longitud

    def __str__(self):
        return self.nombre_completo

class Uso(models.Model):
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion
class MarcaMotor(models.Model):
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion

class MarcaGenerador(models.Model):
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion
class MarcaModulo(models.Model):
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion
class MarcaControlador(models.Model):
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion
class Equipo(models.Model):
    descripcion = models.CharField(max_length=100)
    observaciones = models.CharField(blank=True)
    Horometro = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)  # Campo para latitud
    longitude = models.FloatField(null=True, blank=True)  # Campo para longitud
    Potencia = models.FloatField(null=True, blank=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    uso = models.ForeignKey(Uso, on_delete=models.CASCADE)
    marcamotor = models.ForeignKey(MarcaMotor, on_delete=models.CASCADE)
    marcagenerador = models.ForeignKey(MarcaGenerador, on_delete=models.CASCADE)
    marcamodulo = models.ForeignKey(MarcaModulo, on_delete=models.CASCADE)
    marcacontrolador = models.ForeignKey(MarcaControlador, on_delete=models.CASCADE)

