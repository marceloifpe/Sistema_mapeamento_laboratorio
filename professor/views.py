from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from usuarios.models import Usuario

from salas.models import Salas
from salas.models import Reservas
# @login_required(login_url='/auth/login/?status=2')
# def homee(request):
#     # Obtém o parâmetro 'status' da URL, se presente
#     status = request.GET.get('status')

#     # Verifica se a sessão possui o usuário
#     if 'usuario' in request.session:
#         user_id = request.session['usuario']

#         # Tenta recuperar o usuário do banco de dados
#         try:
#             usuario = Usuario.objects.get(id=user_id)

#             # Passa o objeto de usuário para o contexto do template
#             context = {
#                 'usuario': usuario,
#                 'nome_usuario': usuario.nome,
#             }
#             return render(request, 'homee.html', context)

#         except Usuario.DoesNotExist:
#             # Se o usuário não for encontrado, faça o logout e redirecione para a página de login
#             del request.session['usuario']
#             return redirect('/auth/login/?status=2')

#     # Se 'usuario' não estiver na sessão, algo está errado, faça o logout e redirecione para a página de login
#     return redirect('/auth/login/?status=2')

# def sair(request):
#     request.session.flush()
#     return redirect('/auth/login/')


def homee(request):
    # Verifica se há um usuário na sessão
    if request.session.get('usuario'):
        # Obtém o objeto de usuário com base no ID armazenado na sessão
        usuario = Usuario.objects.get(id=request.session['usuario'])

        # Obtém as salas associadas a esse usuário
        salas = Salas.objects.filter(usuarios=usuario)

        # Renderiza a página inicial com as salas e informações de reservas
        return render(request, 'homee.html', {'salas': salas, 'Reservas': Reservas})

    else:
        # Redireciona para a página de login se não houver usuário na sessão
        return redirect('/auth/login/?status=2')

# Função para visualizar detalhes de uma sala específica
def ver_salas(request, id):
    # Verifica se há um usuário na sessão
    if request.session.get('usuario'):
        # Obtém o objeto de sala com base no ID fornecido
        salas = Salas.objects.get(id=id)

        # Verifica se o usuário na sessão é o mesmo que o usuário associado à sala
        if request.session.get('usuario') == salas.usuarios_id:
            # Renderiza a página de detalhes da sala com informações de reservas
            return render(request, 'ver_salas.html', {'Salas': salas, 'Reservas': Reservas})
        else:
            # Retorna uma resposta indicando que a sala não pertence ao usuário atual
            return HttpResponse('Essa sala não é sua, bandidinho')

    # Redireciona para a página de login se não houver usuário na sessão
    return redirect('/auth/login/?status=2')