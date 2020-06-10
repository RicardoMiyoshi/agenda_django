from django.shortcuts import render, HttpResponse #, redirect # adicionar para utilizar o redirect abaixo
from core.models import Evento

# Create your views here.

def evento(request, titulo_evento):
    evento = Evento.objects.get(titulo=titulo_evento)
    return HttpResponse('<h1>Evento {}, dia {} para o usuário {}</h1>'.format(evento.titulo, evento.data_evento, evento.usuario))

# def index(request):
#     return redirect('/agenda/')

def lista_eventos(request):
    #usuario = request.user # requer que o usuário esteja logado para efetur o filtro por usuário
    #evento = Evento.objects.get(id=1) # faz uma query de acordo com a condição
    evento = Evento.objects.all() # pega toda a lista
    #evento = Evento.objects.filter(usuario=usuario) # filtra por usuario
    data = {'eventos': evento}
    return render(request, 'agenda.html', data)
