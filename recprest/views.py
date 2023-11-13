from django.shortcuts import render
from rest_framework.response import Response
from .models import Newpass
from .serializers import NewpassSerializer
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def recPass(email):
    try:
        usuario = Newpass.objects.get(email=email)
        serializer = NewpassSerializer(usuario)
        credenciales = {
            'email': serializer.data['email'],
            'contraseña': serializer.data['contraseña'],
        }
        return credenciales
    except Newpass.DoesNotExist:
        return None
