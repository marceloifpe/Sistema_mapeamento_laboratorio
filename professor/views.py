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


# def homee(request):
#     if request.session.get('usuario'):
#         usuario = Usuario.objects.get(id = request.session['usuario'])

#         salas = Salas.objects.filter(usuarios=usuario )
#         return render(request, 'homee.html', {'salas': salas, 'reservas': Reservas})

#     else:
#         return redirect('/auth/login/?status = 2')

# def homee(request):
#     # Verifica se há um usuário na sessão
#     if request.session.get('usuario'):
#         # Obtém o objeto de usuário com base no ID armazenado na sessão
#         usuario = Usuario.objects.get(id=request.session['usuario'])

#         # Obtém as reservas associadas a esse usuário
#         reservas = Reservas.objects.filter(quem_reservou=usuario)

#         # Renderiza a página inicial com as informações de reservas
#         return render(request, 'homee.html', {'Reservas': reservas})

#     else:
#         # Redireciona para a página de login se não houver usuário na sessão
#         return redirect('/auth/login/?status=2')

def homee(request):
    # Verifica se há um usuário na sessão
    if request.session.get('usuario'):
        # Obtém o objeto de usuário com base no ID armazenado na sessão
        usuario = Usuario.objects.get(id=request.session['usuario'])

        # Obtém as reservas associadas a esse usuário
        reservas = Reservas.objects.filter(usuarios=usuario)

        # Renderiza a página inicial com as informações de reservas
        return render(request, 'homee.html', {'Reservas': reservas})

    else:
        # Redireciona para a página de login se não houver usuário na sessão
        return redirect('/auth/login/?status=2')



# def ver_salas_professor(request, id):
#     if request.session.get('usuario'):
#         reservas = Reservas.objects.get(id = id)
#         if request.session.get('usuario') == Usuario.id:
#             reservas = Reservas.objects.filter(id = id)
            
#             return render(request, 'ver_salas_professor.html', {'salas': Salas, 'Reservas': reservas})
#         else:
#             return HttpResponse('essa sala nao e sua')
#     return redirect('/auth/login/?status=2')




def ver_salas_professor(request, id):
    # Verifica se há um usuário na sessão
    if request.session.get('usuario'):
        # Obtém o ID do usuário na sessão
        usuario_id = request.session.get('usuario')
        
        # Obtém todas as reservas associadas ao usuário logado e ao ID fornecido
        reservas = Reservas.objects.filter(usuarios_id=usuario_id, id=id,)

        # Verifica se há pelo menos uma reserva pertencente ao usuário logado
        if len(reservas) > 0:
            # Renderiza a página 'ver_salas_professor.html', passando as informações das reservas
            reserva = Reservas.objects.filter(id = id)
            print(reservas)
            return render(request, 'ver_salas_professor.html', {'Reservas': reserva, 'Salas': Salas})
            
            
        else:
            # Se não houver reservas para o usuário logado, retorna uma mensagem de erro
            return HttpResponse('Não há reservas para o usuário logado.')

    # Se não houver usuário na sessão, redireciona para a página de login
    return redirect('/auth/login/?status=2') 







