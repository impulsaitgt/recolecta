from django.db import models

# Create your models here.
class Cliente(models.Model):
    cli_id = models.CharField(max_length=100)
    nombre_completo = models.CharField(null=False)
    latitude = models.FloatField(null=True, blank=True)  # Campo para latitud
    longitude = models.FloatField(null=True, blank=True)  # Campo para longitud
    usuario = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nombre_completo
