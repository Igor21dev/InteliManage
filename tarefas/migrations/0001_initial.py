# Generated by Django 5.0.4 on 2024-04-29 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150)),
                ('descricao', models.TextField()),
                ('completo', models.BooleanField(default=False)),
                ('criadoEm', models.DateTimeField(auto_now_add=True)),
                ('atualizadoEm', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
