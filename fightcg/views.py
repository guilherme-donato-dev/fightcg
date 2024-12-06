from django.views.generic import ListView, DetailView, TemplateView
from django.utils.timezone import now
from .models import Luta, Lutador

# ListView para próximas lutas
class LutasListView(ListView):
    model = Luta
    template_name = 'lista_lutas.html'  # Template para renderizar a lista
    context_object_name = 'lutas'

    def get_queryset(self):
        return Luta.objects.filter(evento__data__gte=now()).order_by('evento__data')


# DetailView para detalhes de uma luta específica
class LutaDetailView(DetailView):
    model = Luta
    template_name = 'detalhes_luta.html'  # Template para renderizar os detalhes
    context_object_name = 'luta'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        luta = self.get_object()
        context['odds'] = self.calcular_odds(luta)  # Odds calculadas
        return context

    def calcular_odds(self, luta):
        # Simples cálculo de odds (substitua com sua lógica real)
        total_apostas = luta.aposta_set.count()
        if total_apostas == 0:
            return {'lutador1': 1.0, 'lutador2': 1.0}
        apostas_lutador1 = luta.aposta_set.filter(lutador_escolhido=luta.lutador1).count()
        apostas_lutador2 = luta.aposta_set.filter(lutador_escolhido=luta.lutador2).count()
        return {
            'lutador1': round(total_apostas / (apostas_lutador1 or 1), 2),
            'lutador2': round(total_apostas / (apostas_lutador2 or 1), 2),
        }


# TemplateView para exibir a equipe técnica de ambos os lutadores
class EquipeTecnicaView(TemplateView):
    template_name = 'equipe_tecnica.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        luta = Luta.objects.get(pk=self.kwargs['pk'])
        context['lutador1'] = luta.lutador1
        context['lutador2'] = luta.lutador2
        context['equipe_tecnica1'] = luta.lutador1.equipe_tecnica_set.all()  # Assumindo que há um modelo relacionado
        context['equipe_tecnica2'] = luta.lutador2.equipe_tecnica_set.all()
        return context

# View para listar a história dos lutadores
class HistoriaLutadoresView(ListView):
    model = Lutador
    template_name = 'historia_lutadores.html'
    context_object_name = 'lutadores'

