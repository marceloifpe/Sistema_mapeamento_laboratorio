from django.shortcuts import render, redirect
from django.http import HttpResponse
from usuarios.models import Usuario

def home(request):
    # Check if the user is logged in
    if request.session.get('usuario'):
        # Retrieve the user object
        user_id = request.session['usuario']
        usuario = Usuario.objects.get(id=user_id)

        # Pass the user object to the template context
        context = {
            'usuario': usuario,
            'nome_usuario': usuario.nome,
        }
        return render(request, 'home.html', context)

    else:
        # Redirect to the login page if the user is not logged in
        return redirect('/auth/login/?status=2')