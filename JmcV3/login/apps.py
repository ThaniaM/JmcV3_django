"""from django.apps import AppConfig
from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.dispatch import receiver

class LoginConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'login'

    @receiver(post_migrate)
    def create_clientes_group(sender, **kwargs):
        from django.contrib.auth.models import Group

        # Crear el grupo "Clientes" si no existe
        clientes_group, created = Group.objects.get_or_create(name='Clientes')

        if created:
            print('Grupo "Clientes" creado exitosamente.')
        else:
            print('El grupo "Clientes" ya existe.')"""
