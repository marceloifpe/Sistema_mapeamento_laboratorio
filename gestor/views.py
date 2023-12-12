# Importando as bibliotecas necessárias
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from usuarios.models import Usuario
from salas.models import Salas
from salas.models import Reservas
from itertools import groupby

# Função para renderizar a página inicial
def home(request):
    # Verifica se há um usuário na sessão
    if request.session.get('usuario'):
        try:
            # Tenta obter o objeto de usuário com base no ID armazenado na sessão
            usuario = Usuario.objects.get(id=request.session['usuario'])

            # Cria um contexto para ser passado para o template
            context = {
                'usuario': usuario,          # Objeto de usuário
                'nome_usuario': usuario.nome, # Atributo 'nome' do usuário
                'salas': Salas.objects.all()   # Obtém todas as instâncias do modelo Salas
            }

            # Renderiza o template 'home.html' com o contexto
            return render(request, 'home.html', context)
        
        except Usuario.DoesNotExist:
            # Trata o caso em que o usuário não existe
            return render(request, 'error.html', {'message': 'Usuário não existe'})

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
                 'salas': Salas.objects.all()   # Obtém todas as instâncias do modelo Salas
             }

             # Renderiza o template 'gestor_ver_salas.html' com o contexto
             return render(request, 'gestor_ver_salas.html', context)

         except Usuario.DoesNotExist:
             # Trata o caso em que o usuário não existe
             return render(request, 'error.html', {'message': 'Usuário não existe'})

     else:
         # Redireciona para a página de login se não houver usuário na sessão
         return redirect('/auth/login/?status=2')

def calendario_reservas(request):
    # Obtenha todas as reservas do banco de dados
    reservas = Reservas.objects.all()

    # Ordene as reservas por data de reserva
    reservas_ordenadas = sorted(reservas, key=lambda x: x.data_reserva)

    # Agrupe as reservas por data de reserva
    grupos_por_data = {data: list(grupo) for data, grupo in groupby(reservas_ordenadas, key=lambda x: x.data_reserva)}

    # Crie uma lista para armazenar os eventos do calendário
    eventos = []

    # Preencha a lista de eventos com os dados de reserva
    # ...

    # ...

    for data, reservas_na_data in grupos_por_data.items():
        eventos_na_data = []
        for reserva in reservas_na_data:
            evento = {
                'title': f"Reserva por {reserva.usuarios.nome} - {reserva.salas.nome_da_sala}",
                'start': reserva.data_reserva.isoformat(),
                'end': reserva.data_devolucao.strftime("%d/%m/%Y"),  # Formate a data de devolução corretamente
                'url': f'/calendario_reservas.html/{reserva.id}',  # Substitua com a URL correta para detalhes da reserva
                'data_solicitacao': reserva.data_solicitacao.strftime("%d/%m/%Y") if reserva.data_solicitacao else None,
            }
            eventos_na_data.append(evento)
        eventos.append({'data': data.strftime("%d/%m/%Y"), 'eventos': eventos_na_data})

    # Renderize o template com os eventos do calendário
    return render(request, 'calendario_reservas.html', {'eventos': eventos})

