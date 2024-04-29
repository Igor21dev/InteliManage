from django.db import models


class Tarefa(models.Model):
    titulo = models.CharField(max_length=150)
    descricao = models.TextField()
    completo = models.BooleanField(default=False)
    criadoEm = models.DateTimeField(auto_now_add=True)
    atualizadoEm = models.DateTimeField(auto_now=True)
    
