from django import forms
from django.forms import ModelForm
from .models import Equipo

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ['id_equipo','tipo_equipo','procesador','tipo_disco', 'uso_disco','marca', 'ram',   'ip_local', 'anydesk', 'nom_usuario', 'nom_antivirus', 'vig_antivirus','office','vig_office','descripcion']
  