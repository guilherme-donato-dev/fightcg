# Generated by Django 5.1.4 on 2024-12-04 23:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('data', models.DateTimeField()),
                ('local', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Luta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_final', models.PositiveIntegerField(blank=True, null=True)),
                ('metodo_vitoria', models.CharField(choices=[('N/A', 'Não Aplicável'), ('KO', 'Nocaute'), ('TKO', 'Nocaute Técnico'), ('Submission', 'Finalização'), ('Decision', 'Decisão')], default='N/A', max_length=100)),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fightcg.evento')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField()),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('luta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fightcg.luta')),
            ],
            options={
                'ordering': ['-criado_em'],
            },
        ),
        migrations.CreateModel(
            name='Lutador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('apelido', models.CharField(blank=True, max_length=100, null=True)),
                ('idade', models.PositiveIntegerField()),
                ('peso', models.FloatField()),
                ('altura', models.FloatField()),
                ('vitorias', models.PositiveIntegerField(default=0)),
                ('derrotas', models.PositiveIntegerField(default=0)),
                ('empates', models.PositiveIntegerField(default=0)),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='fightcg.categoria')),
            ],
        ),
        migrations.AddField(
            model_name='luta',
            name='lutador1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lutas_como_lutador1', to='fightcg.lutador'),
        ),
        migrations.AddField(
            model_name='luta',
            name='lutador2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lutas_como_lutador2', to='fightcg.lutador'),
        ),
        migrations.AddField(
            model_name='luta',
            name='vencedor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lutas_vencidas', to='fightcg.lutador'),
        ),
        migrations.CreateModel(
            name='Aposta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('pago', models.BooleanField(default=False)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('luta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fightcg.luta')),
                ('lutador_escolhido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fightcg.lutador')),
            ],
            options={
                'unique_together': {('usuario', 'luta')},
            },
        ),
    ]
