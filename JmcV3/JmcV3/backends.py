from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class MiBackendPersonalizado(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()

        # Intenta autenticar usando el nombre de usuario
        user = UserModel.objects.filter(username=username).first()

        # Si no se encuentra el usuario, intenta autenticar usando el campo nom_contacto
        if user is None:
            user = UserModel.objects.filter(nom_contacto=username).first()

        # Verifica las credenciales
        if user and user.check_password(password):
            return user
        return None
