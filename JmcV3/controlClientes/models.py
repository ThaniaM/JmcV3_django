from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    # Agrega los campos necesarios para el modelo Usuario

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
    id_usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True)
class Meta:
    managed = True
    db_table = 'cliente'
def __str__(self):
    return f"{self.id_cliente} - {self.nombre}"

