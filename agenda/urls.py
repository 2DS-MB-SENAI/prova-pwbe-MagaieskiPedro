from django.urls import path
from . import views

urlpatterns = [
    path('api/servicos/', view=views.read_servicos, name="Lista todos os serviços disponíveis"),
    path('api/servicos/<int:pk>', view=views.read_servico, name="Detalhes de um serviço específico"),
    path('api/servicos/', view=views.create_servico, name="Cria um novo serviço"),
    path('api/agendamentos', view=views.read_agendamentos, name="Lista todos os agendamentos"),
    path('api/agendamentos/<int:pk>', view=views.read_agendamento, name="Detalhes de um agendamento"),
    path('api/agendamentos', view=views.create_agendamento, name=" Cria novo agendamento"),
]