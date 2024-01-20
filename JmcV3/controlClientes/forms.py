
from django import forms
from django.forms import ModelForm
from .models import Cliente
from django.core.validators import RegexValidator


class ClientesForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["nombre", "direccion", "correo", "telefono", "rfc","rf","cp","municipio","estado","nom_contacto"]
    #RegexValidator, que es una clase proporcionada por Django para validar campos de texto utilizando expresiones regulares.
    

#los métodos clean_<campo> son utilizados para realizar validaciones personalizadas para un campo específico.
def clean_telefono(self):
    telefono = self.cleaned_data.get('telefono')
    telefono_validator = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Ingrese un número de teléfono válido (puede incluir el código de país)."
    )
    return telefono

def clean_nombre(self):
    nombre = self.cleaned_data.get('nombre')
    nombre_validator = RegexValidator(
        regex=r'^[a-zA-Z\s]+$',
        message="El nombre debe contener solo letras y espacios."
    )
    return nombre

def clean_direccion(self):
    direccion = self.cleaned_data.get('direccion')
    direccion_validator = RegexValidator(
        regex=r'^[a-zA-Z0-9\s\-,]+$',
        message="Direccion no valida "
    )    
    return direccion
def clean_cp(self):
    cp= self.cleaned_data.get('cp')
    cp_validator = RegexValidator(
        regex=r'^\d{5}$',
        message="El código postal debe incluir solo 5 digitos"
    )
    return cp
def clean_correo(self):
    correo = self.cleaned_data.get('correo')
    correo_validator = RegexValidator(
        regex=r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',
        message="El correo electronico debe incluir un '@' "
    )
    return correo

def clean_municipio(self):
    municipio = self.cleaned_data.get('municipio')
    municipio_validator = RegexValidator(
        regex=r'^[a-zA-Z\s]+$',
        message="El municipio debe contener solo letras y espacios."
    )
    return municipio
def clean_estado(self):
    estado = self.cleaned_data.get('estado')
    estado_validator = RegexValidator(
        regex=r'^[a-zA-Z\s]+$',
        message="El estado debe contener solo letras y espacios."
    )
    return estado    
def clean_nomContacto(self):
    nom_contacto = self.cleaned_data.get('nom_contacto')
    nom_contacto_validator = RegexValidator(
        regex=r'^[a-zA-Z\s]+$',
        message="El nombre de contacto debe contener solo letras y espacios."
    )
    return nom_contacto

def clean_rfc(self):
    rfc = self.cleaned_data.get('rfc')
    rfc_validator = RegexValidator(
        regex=r'^[A-Z&Ña-z]{4}\d{6}[A-V0-9]{3}$',
        message="RFC invalido"
    )
    return rfc