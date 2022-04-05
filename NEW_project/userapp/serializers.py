from rest_framework import serializers
from .models import *


class StudentPaigeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'phone']
