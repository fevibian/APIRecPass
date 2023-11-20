from rest_framework import status
from django.shortcuts import render
from rest_framework.response import Response
from .models import Newpass
from .serializers import UsuarioSerializer
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import make_password


# Create your views here.

@api_view(['GET'])
def verificar_email(request, email):
    usuario = Newpass.objects.get(email=email)
    serializer = UsuarioSerializer(usuario,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def cambiar_pass(request, pk):
    usuario = Newpass.objects.get(id=pk)
    if not usuario.check_password(request.data.get('contrasena_actual')):
        return Response({'error':'La contraseña actual es incorrecta'},status=status.HTTP_400_BAD_REQUEST)
    nueva_contrasena = request.data.get('nueva_contrasena')
    confirmar_contrasena = request.data.get('confirmar_contrasena')
    if nueva_contrasena != confirmar_contrasena:
        return Response({'error': 'Las nuevas contraseñas no coinciden.'}, status=status.HTTP_400_BAD_REQUEST)
    usuario.set_password(nueva_contrasena)
    usuario.save()
    serializer = UsuarioSerializer(instance=usuario)
    return Response(serializer.data)