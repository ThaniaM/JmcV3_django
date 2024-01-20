from django.urls import path
from django.contrib.auth.decorators import login_required
#from login.views import login_user 

#views
from . import views
urlpatterns = [
    #path('create_clientes',views.create_clientes, name='create_clientes'),
    #path('save', login_required(views.save_clientes), name='save'),
    #path('save', views.save_clientes, name='save'),
    #path('control', login_required(views.listar_clientes), name='control'),
   # path('', views.listar_clientes, name='controlClientes'),
   # path('editar', views.update_clientes, name='editar_clientes'),
    #path('editar/<int:id_cliente>', login_required(views.update_clientes), name='editar_clientes'),
    #path('eliminar/<int:id_cliente>', views.delete_clientes, name='eliminar_clientes'),
    path('create_clientes/', views.create_clientes, name='create_clientes'),
    path('save/', views.save_clientes, name='save'),
    path('', views.listar_clientes, name='controlClientes'),
] 