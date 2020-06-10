from django.contrib import admin
from core.models import Evento

# Register your models here.

class EventoAdmin(admin.ModelAdmin): # customiza a apresentação na página admin to Django
    list_display = ('titulo', 'data_evento', 'data_criacao') 
    list_filter = ('usuario','data_evento',) # necessário manter uma virgula no final da lista

admin.site.register(Evento, EventoAdmin)