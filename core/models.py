from django.db import models
from django.contrib.auth.models import User #importa a tabela de usuário do Django

# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank =True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'evento' # força o nome da tabela como evento, caso contrário ele coloca o nome do app antes de evento, neste caso core_evento

    def __str__(self):
        return self.titulo # para que quando o registro for acessado, o nome do título seja mostrado

    def get_data_evento(self): # altera o formato da data e hora
        return self.data_evento.strftime('%d/%m/%Y %H:%M Hrs')