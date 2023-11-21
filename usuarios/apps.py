from django.apps import AppConfig

class UsuariosConfig(AppConfig):
    # Define o tipo de campo automático padrão como 'BigAutoField'
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Define o nome da aplicação como 'usuarios'
    name = 'usuarios'
