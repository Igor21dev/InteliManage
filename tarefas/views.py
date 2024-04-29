from django.shortcuts import render, redirect
from .models import Tarefa
from .forms import FormularioTarefa

def listaTarefas(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'listaTarefas.html', {'tarefas': tarefas})

def criarTarefa(request):
    if request.method == 'POST':
        formulario = FormularioTarefa(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('listaTarefas')
    else:
        formulario = FormularioTarefa()
        return render(request, 'criarTarefa.html', {'formulario': formulario})
        
        
        
def atualizarTarefa(request, pk):
    tarefa = Tarefa.objects.get(pk=pk)
    if request.method == 'POST':
        formulario = FormularioTarefa(request.POST, instance=tarefa)
        if formulario.is_valid():
            formulario.save()
            return redirect('listaTarefas')
    else:
        formulario = FormularioTarefa(instance=tarefa)
        return render(request, 'atualizarTarefa.html', {'formulario': formulario})
        

def deletarTarefa(request, pk):
    Tarefa.objects.get(pk=pk).delete()
    return redirect('listaTarefas')
