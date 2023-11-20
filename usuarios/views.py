from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
from django.shortcuts import redirect
from hashlib import sha256
import re

def login(request):
    status = request.GET.get('status')
    return render(request,'login.html', {'status': status})

def cadastro(request):
    status = request.GET.get('status')
    return render(request, 'cadastro.html', {'status': status})

def valida_cadastro(request):
    nome = request.POST.get('nome')
    senha = request.POST.get('senha')
    email = request.POST.get('email')

    usuario = Usuario.objects.filter(email=email)

    if len(nome.strip()) == 0 or len(senha.strip()) == 0:
        return redirect('/auth/cadastro/?status=1')

    if not email.endswith('@ufrpe.br'):
        return redirect('/auth/cadastro/?status=2')

    if len(senha) < 8:
        return redirect('/auth/cadastro/?status=3')

    if not re.search(r'[a-z]', senha):  # Pelo menos uma letra minúscula
        return redirect('/auth/cadastro/?status=7')

    if not re.search(r'[A-Z]', senha):  # Pelo menos uma letra maiúscula
        return redirect('/auth/cadastro/?status=8')

    if not re.search(r'[0-9]', senha):  # Pelo menos um número
        return redirect('/auth/cadastro/?status=10')

    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', senha):  # Pelo menos um caractere especial
        return redirect('/auth/cadastro/?status=9')

    if len(usuario) > 0:
        return redirect('/auth/cadastro/?status=4')

    try:
        senha = sha256(senha.encode()).hexdigest()
        usuario = Usuario(nome=nome, senha=senha, email=email)
        usuario.save()

        return redirect('/auth/cadastro/?status=0')
    except:
        return redirect('/auth/cadastro/?status=5')
    
# def valida_login(request):
#     email = request.POST.get('email')
#     senha = request.POST.get('senha')
    
#     senha = sha256(senha.encode()).hexdigest()
    
#     usuario = Usuario.objects.filter(email = email).filter(senha = senha)
    
#     if len(usuario) == 0:
#         return redirect('/auth/login/?status=1')    
#     elif len(usuario)  >= 0:
#         request.session['usuario'] = usuario[0].id
#         return redirect(f'/gestor/home/')
    
#     return HttpResponse(f"{email} {senha}")

def valida_login(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    senha = sha256(senha.encode()).hexdigest()
    usuario = Usuario.objects.filter(email=email).filter(senha=senha)

    if len(usuario) == 0:
        return redirect('/auth/login/?status=1')
    elif len(usuario) >= 0 and usuario[0].email == 'admin@ufrpe.br':
        request.session['usuario'] = usuario[0].id
        return redirect(f'/gestor/home/')
    else:
        return redirect('/admin')#adiciona aqui a url da page home do usuario professor ou servidor
def sair(request):
    request.session.flush()
    return redirect('/auth/login/')
    

# def home_admin(request):
#     return HttpResponse('Seja Bem-Vindo')   

# return redirect(f'/gestor/home/?id_usuario={request.session["usuario"]}') testa id user     
    
    
    
    #teste view de validação de login
# def valida_login(request):
#     email = request.POST.get('email')
#     senha = request.POST.get('senha')
#     return HttpResponse(f"{email} {senha}")


    



#como testar urls criadas
# def login(request):
#     return HttpResponse('login')

# def cadastro(request):
#     return HttpResponse('cadastro')
    