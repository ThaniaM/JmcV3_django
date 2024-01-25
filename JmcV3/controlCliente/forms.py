#forms
from django import forms
from django.forms import ModelForm
from .models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["id_cliente","nombre",  "correo","direccion", "telefono", "rfc","cp","estado","nom_contacto",]
#el formulario va dependiendo los campops del modelo y los formularios usados en los modales
        #nita: respetar el orden para que funcione