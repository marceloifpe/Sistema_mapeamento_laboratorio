# Importando as bibliotecas necessárias
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from materiais.models import Materiais, Reserva
from usuarios.models import Usuario
from salas.models import Salas
from salas.models import Reservas

# Função para renderizar a página inicial
def home(request):
    # Verifica se há um usuário na sessão
    if request.session.get('usuario'):
        # Obtém o objeto de usuário com base no ID armazenado na sessão
        usuario = Usuario.objects.get(id=request.session['usuario'])

        # Obtém as reservas de materiais associadas a esse usuário
        reservas_materiais = Reserva.objects.filter(usuarios=usuario)

        # Renderiza a página inicial com as informações de reservas
        return render(request, 'home.html', {
            'ReservasSalas': reservas_salas,
            'ReservasMateriais': reservas_materiais,
            'usuario_logado2': usuario,
        })

    else:
        # Redireciona para a página de login se não houver usuário na sessão
        return redirect('/auth/login/?status=2')
# Função para o gestor visualizar as salas
def gestor_ver_salas(request):
    # Verifica se há um usuário na sessão
    if request.session.get('usuario'):
        try:
            # Tenta obter o objeto de usuário com base no ID armazenado na sessão
            usuario = Usuario.objects.get(id=request.session['usuario'])

            # Cria um contexto para ser passado para o template
            context = {
                'usuario': usuario,          # Objeto de usuário
                'nome_usuario': usuario.nome, # Atributo 'nome' do usuário
                'salas': Salas.objects.filter(reservado=True),   # Obtém todas as instâncias do modelo Salas
                'usuario_logado2': usuario          
            }

            # Renderiza o template 'gestor_ver_salas.html' com o contexto
            return render(request, 'gestor_ver_salas.html', context)

        except Usuario.DoesNotExist:
            # Trata o caso em que o usuário não existe
            return render(request, 'error.html', {'message': 'Usuário não existe'})

    else:
        # Redireciona para a página de login se não houver usuário na sessão
        return redirect('/auth/login/?status=2')
    
def gestor_ver_materiais(request):
     if request.session.get('usuario'):
      try:
        usuario = Usuario.objects.get(id=request.session['usuario'])

        context = {
                'usuario': usuario,
                'nome_usuario': usuario.nome,
                'materiais': Materiais.objects.filter(reservado=True),
                'usuario_logado2': usuario
            }

        return render(request, 'gestor_ver_materiais.html', context)
      except Usuario.DoesNotExist:
            # Trata o caso em que o usuário não existe
            return render(request, 'error.html', {'message': 'Usuário não existe'})

     else:
        # Redireciona para a página de login se não houver usuário na sessão
        return redirect('/auth/login/?status=2')