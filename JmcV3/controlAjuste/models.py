# models.py

from django.db import models

class Cliente(models.Model):
    # Define your Cliente model fields here
    pass

class Staff(models.Model):
    # Define your Staff model fields here
    pass

class Contrato(models.Model):
    # Define your Contrato model fields here
    pass

class Pago(models.Model):
    fecha = models.DateField(null=True, blank=True)
    pdf = models.BinaryField(null=True, blank=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)
    id_staff = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True, blank=True)
    id_contrato = models.ForeignKey(Contrato, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Pago {self.id_pago}"
