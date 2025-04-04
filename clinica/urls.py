from django.urls import path
from . import views

urlpatterns = [
    path('medicos/', view=views.listar_medicos, name="Lista todos os médicos cadastrados"),
    path('consultas/nova/', view=views.criar_consulta, name="Agendamento"),
    path('consultas/<int:id>/', view=views.detalhes_consulta, name="Detalhes da consulta")
]