# Importando as bibliotecas necessárias
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from usuarios.models import Usuario
from salas.models import Reservas
from materiais.models import Reserva
from .forms import RealizarReservas, RealizarReserva

# Função para renderizar a página inicial
def homee(request):
    # Verifica se há um usuário na sessão
    if request.session.get('usuario'):
        # Obtém o objeto de usuário com base no ID armazenado na sessão
        usuario = Usuario.objects.get(id=request.session['usuario'])

        # Obtém as reservas de salas associadas a esse usuário
        reservas_salas = Reservas.objects.filter(usuarios=usuario)

        # Obtém as reservas de materiais associadas a esse usuário
        reservas_materiais = Reserva.objects.filter(usuarios=usuario)

        form_salas = RealizarReservas()
        form_salas.fields['usuarios'].initial = request.session['usuario']

        form_materiais = RealizarReserva()
        form_materiais.fields['usuarios'].initial = request.session['usuario']

        # Renderiza a página inicial com as informações de reservas
        return render(request, 'homee.html', {'ReservasSalas': reservas_salas, 'ReservasMateriais': reservas_materiais, 'usuario_logado': request.session.get('usuario'), 'form_salas': form_salas, 'form_materiais': form_materiais})

    else:
        # Redireciona para a página de login se não houver usuário na sessão
        return redirect('/auth/login/?status=2')


# Função para o professor visualizar as salas
def ver_salas_professor(request, id):
    # Verifica se há um usuário na sessão
    if request.session.get('usuario'):
        # Obtém o ID do usuário na sessão
        usuario_id = request.session.get('usuario')

        # Obtém todas as reservas associadas ao usuário logado e ao ID fornecido
        reservas = Reservas.objects.filter(usuarios_id=usuario_id, id=id)
        form_salas = RealizarReservas()

        # Verifica se há pelo menos uma reserva pertencente ao usuário logado
        if len(reservas) > 0:
            # Renderiza a página 'ver_salas_professor.html', passando as informações das reservas
            return render(request, 'ver_salas_professor.html', {'Reservas': reservas, 'usuario_logado': request.session.get('usuario'), 'form_salas': form_salas})

        else:
            # Se não houver reservas para o usuário logado, retorna uma mensagem de erro
            return HttpResponse('Não há reservas para o usuário logado.')

    else:
        # Se não houver usuário na sessão, redireciona para a página de login
        return redirect('/auth/login/?status=2')

# Função para realizar a reserva de salas
def realizar_reserva_salas(request):
    if request.method == 'POST':
        form_salas = RealizarReservas(request.POST)
        if form_salas.is_valid():
            form_salas.save()
            return HttpResponse(request.POST)
        else:
            return HttpResponse('Dados inválidos')

# Função para o professor visualizar os materiais
def ver_materiais_professor(request, id):
    # Verifica se há um usuário na sessão
    if request.session.get('usuario'):
        # Obtém o ID do usuário na sessão
        usuario_id = request.session.get('usuario')

        # Obtém todas as reservas associadas ao usuário logado e ao ID fornecido
        reserva = Reserva.objects.filter(usuarios_id=usuario_id, id=id)
        form_materiais = RealizarReserva()

        # Verifica se há pelo menos uma reserva pertencente ao usuário logado
        if len(reserva) > 0:
            # Renderiza a página 'ver_materiais_professor.html', passando as informações das reservas
            return render(request, 'ver_materiais_professor.html', {'Reserva': reserva, 'usuario_logado': request.session.get('usuario'), 'form_materiais': form_materiais})

        else:
            # Se não houver reservas para o usuário logado, retorna uma mensagem de erro
            return HttpResponse('Não há reservas para o usuário logado.')

    else:
        # Se não houver usuário na sessão, redireciona para a página de login
        return redirect('/auth/login/?status=2')

# Função para realizar a reserva de materiais
def realizar_reserva_materiais(request):
    if request.method == 'POST':
        form_materiais = RealizarReserva(request.POST)
        if form_materiais.is_valid():
            form_materiais.save()
            return HttpResponse(request.POST)
        else:
            return HttpResponse('Dados inválidos')
