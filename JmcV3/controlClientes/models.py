from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80)
    direccion = models.CharField(max_length=100, null=True, blank=True)
    correo = models.EmailField(null=True, blank=True)
    telefono = models.CharField(max_length=10, null=True, blank=True)
    rfc = models.CharField(max_length=13, null=True, blank=True)
    rf = models.CharField(max_length=45, null=True, blank=True)
    cp = models.CharField(max_length=5)
    municipio = models.CharField(max_length=50, null=True, blank=True)
    estado = models.CharField(max_length=50, null=True, blank=True)
    nom_contacto = models.CharField(max_length=50)
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nombre
