from django.shortcuts import redirect, render
from django.http import HttpResponse
from usuarios.models import Usuario

def home(request):
    # Check if the user is logged in
    if request.session.get('usuario'):
        # Retrieve the user object
        user_id = request.session['usuario']
        usuario = Usuario.objects.get(id=user_id)

        # Display a personalized greeting with the username
        return HttpResponse(f'Oi Gestor {usuario.nome}, seja bem-vindo !')

    else:
        # Redirect to the login page if the user is not logged in
        return redirect('/auth/login/?status=2')
