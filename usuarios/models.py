from django.db import models

class Usuario(models.Model):
    # Define um campo de caractere para o nome do usuário com no máximo 50 caracteres
    nome = models.CharField(max_length=50)
    
    # Define um campo de e-mail para o e-mail do usuário
    email = models.EmailField()
    
    # Define um campo de caractere para a senha do usuário com no máximo 64 caracteres
    senha = models.CharField(max_length=64)

    # Define o método __str__ para retornar uma representação de string do objeto
    def __str__(self) -> str:
        return self.nome
