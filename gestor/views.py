# Importando as bibliotecas necessárias
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from materiais.models import Materiais, Reserva
from usuarios.models import Usuario
from salas.models import Salas
from salas.models import Reservas
from itertools import groupby
from django.contrib import messages

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
                'salas': Salas.objects.all(),   # Obtém todas as instâncias do modelo Salas
                'usuario_logado2': usuario,
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
                'usuario': usuario,             # Objeto de usuário
                'nome_usuario': usuario.nome,   # Atributo 'nome' do usuário
                'salas': Salas.objects.all(),   # Obtém todas as instâncias do modelo Salas
                'usuario_logado2': usuario
            }

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
                'materiais': Materiais.objects.all(),
                'usuario_logado2': usuario
            }

            return render(request, 'gestor_ver_materiais.html', context)
        except Usuario.DoesNotExist:
            # Trata o caso em que o usuário não existe
            return render(request, 'error.html', {'message': 'Usuário não existe'})
    else:
        # Redireciona para a página de login se não houver usuário na sessão
        return redirect('/auth/login/?status=2')
    
def calendario_reservas(request):
     # Verifica se há um usuário na sessão
    if request.session.get('usuario'):
        try:
            # Obtém o objeto de usuário com base no ID armazenado na sessão
            usuario = Usuario.objects.get(id=request.session['usuario'])

            # Obtenha todas as reservas do banco de dados (tanto de salas quanto de materiais)
            reservas_salas = Reservas.objects.filter(salas__isnull=False)
            reservas_materiais = Reserva.objects.filter(materiais__isnull=False)

            # Combine as duas listas de reservas
            reservas = list(reservas_salas) + list(reservas_materiais)

            # Ordene as reservas por data de reserva
            reservas_ordenadas = sorted(reservas, key=lambda x: x.data_reserva)

            # Agrupe as reservas por data de reserva
            grupos_por_data = {data: list(grupo) for data, grupo in groupby(reservas_ordenadas, key=lambda x: x.data_reserva)}

            # Crie uma lista para armazenar os eventos do calendário
            eventos = []

            for data, reservas_na_data in grupos_por_data.items():
                eventos_na_data = []
                for reserva in reservas_na_data:
                    # Determine se a reserva é de sala ou material
                    tipo_reserva = "Sala" if hasattr(reserva, 'salas') else "Material"
                    
                    evento = {
                        'title': f"Reserva de {tipo_reserva} por {reserva.usuarios.nome} - {reserva.salas.nome_da_sala if tipo_reserva == 'Sala' else reserva.materiais.nome_do_material}",
                        'start': reserva.data_reserva.isoformat(),
                        'end': reserva.data_devolucao.strftime("%d/%m/%Y"),
                        'url': f'/calendario_reservas.html/{reserva.id}',
                        'data_solicitacao': reserva.data_solicitacao.strftime("%d/%m/%Y") if reserva.data_solicitacao else None,
                        'tipo_reserva': tipo_reserva,
                    }
                    eventos_na_data.append(evento)
                eventos.append({'data': data.strftime("%d/%m/%Y"), 'eventos': eventos_na_data})

            # Renderize o template com os eventos do calendário
            return render(request, 'calendario_reservas.html', {'eventos': eventos, 'usuario_logado2': usuario})

        except Usuario.DoesNotExist:
            # Trata o caso em que o usuário não existe
            messages.error(request, 'Usuário não encontrado.')
            return render(request, 'error.html', {'message': 'Usuário não existe'})
    else:
        # Redireciona para a página de login se não houver usuário na sessão
        messages.warning(request, 'Faça login para acessar o calendário de reservas.')
        return redirect('/auth/login/?status=2')

