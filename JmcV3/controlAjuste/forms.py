""" from django import forms
from django.forms import ModelForm
from .models import Servicio


class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ["id_servicio","nombre_servicio","descripcion","costo", "plan",]
#el formulario va dependiendo los campops del modelo y los formularios usados en los modales
        #nita: respetar el orden para que funcione
        


 """