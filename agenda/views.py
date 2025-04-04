from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view 
from rest_framework import status

from .models import Servico,Agendamento
from .serializer import ServicoSerializer,AgendamentoSerializer

# servicos######################################################
@api_view(['GET'])
def read_servicos(request):
    servicos = Servico.objects.all()
    serializer = ServicoSerializer(servicos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def read_servico(request,pk):
    try:
        servico = Servico.objects.get(pk=pk)
    except Servico.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    serializer = ServicoSerializer(servico)
    return Response(serializer.data)

@api_view(['POST'])
def create_servico(request):
    serializer = ServicoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


#agendamentos####################################################
@api_view(['GET'])
def read_agendamentos(request):
    agendamentos = Agendamento.objects.all()
    serializer = AgendamentoSerializer(agendamentos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def read_agendamento(request,pk):
    try:
        agendamento = Agendamento.objects.get(pk=pk)
    except Agendamento.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    serializer = AgendamentoSerializer(agendamento)
    return Response(serializer.data)

@api_view(['POST'])
def create_agendamento(request):
    serializer = AgendamentoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)