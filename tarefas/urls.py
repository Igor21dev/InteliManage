from django.urls import path
from . import views

urlpatterns = [
    path('', views.listaTarefas, name='listaTarefas'),
    path('criar/', views.criarTarefa, name='criar'),
    path('<int:pk>/atualizar/', views.atualizarTarefa, name='atualizarTarefa'),
    path('<int:pk>/deletar/', views.deletarTarefa, name='deletarTarefa'),
]
