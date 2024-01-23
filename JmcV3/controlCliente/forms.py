#forms
from django import forms
from django.forms import ModelForm
from .models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["id_cliente","nombre",  "correo","direccion", "telefono", "rfc","cp","municipio","estado","nom_contacto",]
