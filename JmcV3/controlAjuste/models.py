from django.db import models

class Servicio(models.Model):
    id_servicio = models.AutoField(primary_key=True)
    nombre_servicio = models.CharField(max_length=80)
    descripcion = models.CharField(max_length=600, null=True, blank=True)
    costo = models.CharField(max_length=20, null=True, blank=True)
    plan = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        managed = True