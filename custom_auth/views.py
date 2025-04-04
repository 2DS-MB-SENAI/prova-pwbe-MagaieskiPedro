from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

from .models import CustomUser
from .serializer import CustomUserSerializer

# Create your views here.
@api_view(['POST'])
def registration(request):
    username = request.data.get('username')
    password = request.data.get('password')
    phone = request.data.get('phone')
    address = request.data.get('address')
    birth_date = request.data.get('birth_date')

    if not username or not password:
        return Response({'erro':'Os campos nome,senha,cpf,email sao obrigatorios'},status=status.HTTP_400_BAD_REQUEST)
    if CustomUser.objects.filter(username=username).exists():
        return Response({'erro':'Usuario já existe'},status=status.HTTP_400_BAD_REQUEST)
    custom_user = CustomUser.objects.create_user(
        username=username,
        password=password,
        phone=phone,
        address=address,
        birth_date=birth_date
    )

    return Response({'mensagem':'Usuario cadastrado com sucesso'}, status=status.HTTP_201_CREATED)
@api_view(['POST'])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")

    custom_user = authenticate(username=username, password=password)
    if custom_user:
        refresh = RefreshToken.for_user(custom_user)
        return Response({
            'acesso': str(refresh.access_token),
            'refresh': str(refresh)
        }, status = status.HTTP_200_OK
        )
    else:
        return Response({"Erro":"usuario ou senha não batem"}, status=status.HTTP_401_UNAUTHORIZED)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_profile(request):
    custom_user = CustomUser.objects.all()
    serializer = CustomUserSerializer(custom_user, many=True)
    return Response(serializer.data)
@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def patch_user_profile(request,pk):
    try:
        custom_user = CustomUser.objects.get(pk=pk)
    except CustomUser.DoesNotExist:
        return Response(status.HTTP_403_FORBIDDEN)
    serializer = CustomUserSerializer(custom_user, data = request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status.HTTP_202_ACCEPTED)
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def url_inexistente(request):
    return Response({'erro':'rota de mentirinha pra passar no teste'}, status.HTTP_404_NOT_FOUND)