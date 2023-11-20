from rest_framework import serializers
from .models import Newpass

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newpass
        fields = ['email', 'password']