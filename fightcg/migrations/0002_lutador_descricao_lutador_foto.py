# Generated by Django 5.1.4 on 2024-12-05 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fightcg', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lutador',
            name='descricao',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='lutador',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='lutadores/'),
        ),
    ]
