from django.urls import path

#vistas
from . import views

#configurar url
#despues del ciews. es el nombre que se pone en la funcion en el archivo vistas
urlpatterns = [
  path('', views.controlClientes, name='controlClientes'),
]