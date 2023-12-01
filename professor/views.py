from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from usuarios.models import Usuario

from salas.models import Salas
from salas.models import Reservas
from django.shortcuts import get_object_or_404, redirect, render, reverse
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



def ver_salas(request, id):
    if request.session.get('usuario'):
        salas = Reservas.objects.get(id=id)
        if request.session.get('usuario') == salas.usuarios_id:
            # Obtém as reservas da sala
            reservas = salas.reservas
            # Passa a sala e as reservas para o contexto
            return render(request, 'ver_salas.html', {'sala': salas, 'reservas': reservas})
        else:
           return HttpResponse(' essa sala nao e tua bandidinho')

    return redirect('/auth/login/?status = 2')

# def ver_salas(request, id):
#     if request.session.get('usuario'):
#         salas = Salas.objects.get(id=id)
#         if request.session.get('usuario') == salas.usuarios_id:
#             # Obtém as reservas da sala
#             reservas = Reservas.objects.filter(salas=salas)
#             # Passa a sala e as reservas para o contexto
#             return render(request, 'ver_salas.html', {'sala': salas, 'reservas': reservas})
#         else:
#            return HttpResponse(' essa sala nao e tua bandidinho')

#     return redirect('/auth/login/?status = 2')




# def ver_salas(request, id):
#     if request.session.get('usuario'):
#         salas = Salas.objects.get(id=id)
#         if request.session.get('usuario') == salas.usuarios_id:
#             return render(request, 'ver_salas.html', {'Reservas': Reservas})
#         else:
#            return HttpResponse(' essa sala nao e tua bandidinho')

#     return redirect('/auth/login/?status = 2')

