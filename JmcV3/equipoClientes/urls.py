from django.urls import path
#vistas
from . import views
urlpatterns = [
  path('', views.equipoCliente, name='equipoCliente'),
]
