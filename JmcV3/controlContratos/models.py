from django.db import models

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    # Agrega los campos necesarios para el modelo Cliente

class Servicio(models.Model):
    id_servicio = models.AutoField(primary_key=True)
    # Agrega los campos necesarios para el modelo Servicio

class Contrato(models.Model):
    id_contrato = models.AutoField(primary_key=True)
    fecha_contrato = models.DateField(null=True, blank=True)
    status_contrato = models.CharField(max_length=20, null=True, blank=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)
    id_servicio = models.ForeignKey(Servicio, on_delete=models.SET_NULL, null=True, blank=True)

class Meta:
        managed = True
        db_table = 'contrato'
        
def __str__(self):
    return f"{self.id_contrato} - {self.id_cliente} - {self.id_servicio}"
