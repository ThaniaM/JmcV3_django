from django.db import models

class Cliente(models.Model):
    # campos del modelo Cliente
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
 
class Staff(models.Model):
    #campos de modelo Staff
  id_staff = models.AutoField(primary_key=True)
  nombre = models.CharField(max_length=80, null=True, blank=True)
  telefono = models.CharField(max_length=10, null=True, blank=True)
  departamento = models.CharField(max_length=30, null=True, blank=True)

class Contrato(models.Model):
    #campos  modelo Contrato 
  id_contrato = models.AutoField(primary_key=True)
  fecha_contrato = models.DateField(null=True, blank=True)
  status_contrato = models.CharField(max_length=20, null=True, blank=True)

class Pago(models.Model):
  fecha = models.DateField(null=True, blank=True)
  pdf = models.BinaryField(null=True, blank=True)
  id_cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)
  id_staff = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True, blank=True)
  id_contrato = models.ForeignKey(Contrato, on_delete=models.SET_NULL, null=True, blank=True)
class Meta:
    managed = True
    db_table = 'pago'
def __str__(self):
    return f'Pago {self.id_pago}'
