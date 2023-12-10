# Importando as bibliotecas necessárias
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from usuarios.models import Usuario
from salas.models import Salas
from salas.models import Reservas
from materiais.models import Materiais
from materiais.models import Reserva
from .forms import RealizarReservas
from .forms import RealizarReserva

# Função para renderizar a página inicial
def homee(request):
    # Verifica se há um usuário na sessão
    if request.session.get('usuario'):
        # Obtém o objeto de usuário com base no ID armazenado na sessão
        usuario = Usuario.objects.get(id=request.session['usuario'])

        # Obtém as reservas associadas a esse usuário e as ordena pelo nome da sala
        reservas = Reservas.objects.filter(usuarios=usuario).order_by('data_solicitacao')
        reserva = Reserva.objects.filter(usuarios=usuario)
        form = RealizarReservas()
        form.fields['usuarios'].initial = request.session['usuario']

        # Renderiza a página inicial com as informações de reservas
        return render(request, 'homee.html', {'Reservas': reservas, 'usuario_logado': request.session.get('usuario'), 'form': form, 'Reserva': reserva})

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
        form = RealizarReservas()

        # Verifica se há pelo menos uma reserva pertencente ao usuário logado
        if len(reservas) > 0:
            # Renderiza a página 'ver_salas_professor.html', passando as informações das reservas
            return render(request, 'ver_salas_professor.html', {'Reservas': reservas, 'usuario_logado': request.session.get('usuario'), 'form': form})

        else:
            # Se não houver reservas para o usuário logado, retorna uma mensagem de erro
            return HttpResponse('Não há reservas para o usuário logado.')

    else:
        # Se não houver usuário na sessão, redireciona para a página de login
        return redirect('/auth/login/?status=2')

# Função para realizar a reserva de salas
def realizar_reserva_salas(request):
    if request.method =='POST':
        form = RealizarReservas(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/professor/reserva_sucesso/')

        else:
            return HttpResponse('dados invalidos')

# Função para o professor visualizar os materiais
def ver_materiais_professor(request, id):
    # Verifica se há um usuário na sessão
    if request.session.get('usuario'):
        # Obtém o ID do usuário na sessão
        usuario_id = request.session.get('usuario')

        # Obtém todas as reservas associadas ao usuário logado e ao ID fornecido
        reserva = Reserva.objects.filter(usuarios_id=usuario_id, id=id)
        form = RealizarReserva()

        # Verifica se há pelo menos uma reserva pertencente ao usuário logado
        if len(reserva) > 0:
            # Renderiza a página 'ver_salas_professor.html', passando as informações das reservas
            return render(request, 'ver_materiais_professor.html', {'Reserva': reserva, 'usuario_logado': request.session.get('usuario'), 'form': form})

        else:
            # Se não houver reservas para o usuário logado, retorna uma mensagem de erro
            return HttpResponse('Não há reservas para o usuário logado.')

    else:
        # Se não houver usuário na sessão, redireciona para a página de login
        return redirect('/auth/login/?status=2')

# Função para realizar a reserva de materiais
def realizar_reserva_materiais(request):
    if request.method =='POST':
        form = RealizarReserva(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(request.POST)
        else:
            return HttpResponse('dados invalidos')
