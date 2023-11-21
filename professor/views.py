from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from usuarios.models import Usuario

@login_required(login_url='/auth/login/?status=2')
def homee(request):
    # Obtém o parâmetro 'status' da URL, se presente
    status = request.GET.get('status')

    # Verifica se a sessão possui o usuário
    if 'usuario' in request.session:
        user_id = request.session['usuario']

        # Tenta recuperar o usuário do banco de dados
        try:
            usuario = Usuario.objects.get(id=user_id)

            # Passa o objeto de usuário para o contexto do template
            context = {
                'usuario': usuario,
                'nome_usuario': usuario.nome,
            }
            return render(request, 'homee.html', context)

        except Usuario.DoesNotExist:
            # Se o usuário não for encontrado, faça o logout e redirecione para a página de login
            del request.session['usuario']
            return redirect('/auth/login/?status=2')

    # Se 'usuario' não estiver na sessão, algo está errado, faça o logout e redirecione para a página de login
    return redirect('/auth/login/?status=2')
