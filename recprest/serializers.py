from rest_framework import serializers
from .models import Newpass

class NewpassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newpass
        fields = '__all__'