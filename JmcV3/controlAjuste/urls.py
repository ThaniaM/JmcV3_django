from django.urls import path
from django.contrib.auth.decorators import login_required #que sea necesario iniciar sesion

from . import views
urlpatterns = [
    path('create_servicio',views.create_servicio, name='create_servicio'),
    path('listar_servicio', login_required (views.listar_servicio), name='listar_servicio'),
    path('editar_servicio/<int:id_servicio>', login_required (views.update_servicio), name='editar_servicio'),
    path('eliminar/<int:id_servicio>', views.delete_servicio, name='eliminar_servicio'),
] 





