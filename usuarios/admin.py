from django.contrib import admin
from .models import Usuario

# Registra o modelo 'Usuario' no painel de administração
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    # Define os campos 'nome', 'email' e 'senha' como somente leitura na interface de administração
    readonly_fields = ('nome', 'email', 'senha')
