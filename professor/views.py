from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from usuarios.models import Usuario

from salas.models import Salas
from salas.models import Reservas

def homee(request):
    # Verifica se há um usuário na sessão
    if request.session.get('usuario'):
        # Obtém o objeto de usuário com base no ID armazenado na sessão
        usuario = Usuario.objects.get(id=request.session['usuario'])

        # Obtém as reservas associadas a esse usuário
        reservas = Reservas.objects.filter(usuarios=usuario)

        # Renderiza a página inicial com as informações de reservas
        return render(request, 'homee.html', {'Reservas': reservas, 'usuario_logado': request.session.get('usuario')})

    else:
        # Redireciona para a página de login se não houver usuário na sessão
        return redirect('/auth/login/?status=2')





def ver_salas_professor(request, id):
    # Verifica se há um usuário na sessão
    if request.session.get('usuario'):
        # Obtém o ID do usuário na sessão
        usuario_id = request.session.get('usuario')


        # Obtém todas as reservas associadas ao usuário logado e ao ID fornecido
        reservas = Reservas.objects.filter(usuarios_id=usuario_id, id=id)
        
        # Obtém todas as reservas associadas ao usuário logado e ao ID fornecido
        # reservas = Reservas.objects.filter(usuarios_id=usuario_id, id=id,)


        # Verifica se há pelo menos uma reserva pertencente ao usuário logado
        if len(reservas) > 0:
            # Renderiza a página 'ver_salas_professor.html', passando as informações das reservas

            return render(request, 'ver_salas_professor.html', {'Reservas': reservas, 'usuario_logado': request.session.get('usuario')})
            reserva = Reservas.objects.filter(id = id)
            print(reservas)
            return render(request, 'ver_salas_professor.html', {'Reservas': reserva, 'Salas': Salas, 'usuario_logado': request.session.get('usuario')})
            
 
        else:
            # Se não houver reservas para o usuário logado, retorna uma mensagem de erro
            return HttpResponse('Não há reservas para o usuário logado.')

    # Se não houver usuário na sessão, redireciona para a página de login
    return redirect('/auth/login/?status=2') 





# def professor(request, id):
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






