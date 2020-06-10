from django.shortcuts import render, redirect # adicionar para utilizar o redirect abaixo
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

# def index(request):
#     return redirect('/agenda/')

def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou senha inválido")
    
    return redirect('/')

@login_required(login_url='/login/')
def lista_eventos(request):
    usuario = request.user # requer que o usuário esteja logado para efetur o filtro por usuário
    #evento = Evento.objects.get(id=1) # faz uma query de acordo com a condição
    #evento = Evento.objects.all() # pega toda a lista
    evento = Evento.objects.filter(usuario=usuario) # filtra por usuario
    data = {'eventos': evento}
    return render(request, 'agenda.html', data)
