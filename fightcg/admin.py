from django.contrib import admin
from .models import Categoria, Lutador, Evento, Luta, Aposta, Comentario

# Configuração básica para exibir todos os campos no Admin
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')
    search_fields = ('nome',)

@admin.register(Lutador)
class LutadorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'apelido', 'idade', 'peso', 'altura', 'vitorias', 'derrotas', 'empates', 'categoria')
    search_fields = ('nome', 'apelido')
    list_filter = ('categoria',)
    ordering = ('nome',)

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data', 'local')
    search_fields = ('nome', 'local')
    list_filter = ('data',)

@admin.register(Luta)
class LutaAdmin(admin.ModelAdmin):
    list_display = ('evento', 'lutador1', 'lutador2', 'vencedor', 'round_final', 'metodo_vitoria')
    search_fields = ('evento__nome', 'lutador1__nome', 'lutador2__nome')
    list_filter = ('evento', 'metodo_vitoria')
    ordering = ('-evento__data',)

@admin.register(Aposta)
class ApostaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'luta', 'lutador_escolhido', 'valor', 'criado_em', 'pago')
    search_fields = ('usuario__username', 'luta__evento__nome', 'lutador_escolhido__nome')
    list_filter = ('pago', 'criado_em')

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'luta', 'texto', 'criado_em')
    search_fields = ('usuario__username', 'luta__evento__nome', 'texto')
    list_filter = ('criado_em',)
