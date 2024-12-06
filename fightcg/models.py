from django.db import models
from django.contrib.auth.models import User

# Modelo para categorias de luta (peso, estilo, etc.)
class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

# Modelo para lutadores
class Lutador(models.Model):
    nome = models.CharField(max_length=100)
    apelido = models.CharField(max_length=100, blank=True, null=True)
    idade = models.PositiveIntegerField()
    peso = models.FloatField()
    altura = models.FloatField()
    descricao = models.TextField(null=True)  # Campo para a história
    foto = models.ImageField(upload_to='lutadores/', blank=True, null=True)  # Foto do lutador
    vitorias = models.PositiveIntegerField(default=0)
    derrotas = models.PositiveIntegerField(default=0)
    empates = models.PositiveIntegerField(default=0)
    categoria = models.ForeignKey('Categoria', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nome

# Modelo para eventos de luta
class Evento(models.Model):
    nome = models.CharField(max_length=200)
    data = models.DateTimeField()
    local = models.CharField(max_length=200)
    

    def __str__(self):
        return self.nome

# Modelo para lutas
class Luta(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    lutador1 = models.ForeignKey(Lutador, on_delete=models.CASCADE, related_name='lutas_como_lutador1')
    lutador2 = models.ForeignKey(Lutador, on_delete=models.CASCADE, related_name='lutas_como_lutador2')
    vencedor = models.ForeignKey(Lutador, on_delete=models.SET_NULL, null=True, blank=True, related_name='lutas_vencidas')  # Altere o related_name aqui
    round_final = models.PositiveIntegerField(blank=True, null=True)
    foto = models.ImageField(upload_to='lutas/', blank=True, null=True)
    metodo_vitoria = models.CharField(
        max_length=100, 
        choices=[
            ('N/A', 'Não Aplicável'),
            ('KO', 'Nocaute'),
            ('TKO', 'Nocaute Técnico'),
            ('Submission', 'Finalização'),
            ('Decision', 'Decisão')
        ],
        default='N/A'
    )

    def __str__(self):
        return f"{self.lutador1} vs {self.lutador2} - {self.evento.nome}"




# Modelo para apostas
class Aposta(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Usuário que faz a aposta
    luta = models.ForeignKey(Luta, on_delete=models.CASCADE)  # Luta relacionada
    lutador_escolhido = models.ForeignKey(Lutador, on_delete=models.CASCADE)  # Lutador escolhido para vencer
    valor = models.DecimalField(max_digits=10, decimal_places=2)  # Valor da aposta
    criado_em = models.DateTimeField(auto_now_add=True)
    pago = models.BooleanField(default=False)  # Indica se a aposta foi paga

    def __str__(self):
        return f"Aposta de {self.usuario} em {self.lutador_escolhido} para {self.luta}"

    class Meta:
        unique_together = ('usuario', 'luta')  # Um usuário só pode apostar uma 


    # Modelo para comentários
class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Usuário que fez o comentário
    luta = models.ForeignKey(Luta, on_delete=models.CASCADE)  # Luta relacionada
    texto = models.TextField()  # Conteúdo do comentário
    criado_em = models.DateTimeField(auto_now_add=True)  # Data e hora do comentário

    def __str__(self):
        return f"Comentário de {self.usuario} em {self.luta}"

    class Meta:
        ordering = ['-criado_em']  # Comentários mais recentes aparecem primeiro
