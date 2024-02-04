from django.contrib.auth.backends import ModelBackend
from controlCliente.models import Cliente
from django.contrib.auth.hashers import check_password

class ClienteBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Intenta autenticar con el modelo de Cliente personalizado
            user = Cliente.objects.get(nom_contacto=username)
            
            # Utiliza check_password para comparar las contraseñas
            if check_password(password, user.password):
                return user
        except Cliente.DoesNotExist:
            pass

        # Si no se encuentra en el modelo de Cliente, utiliza el backend de autenticación predeterminado
        return super().authenticate(request, username=username, password=password, **kwargs)
