from rest_framework import serializers
from .models import *
from eduapp.models import *
from userapp.models import *


class ResultSerializer(serializers.ModelSerializer):
    user_phone = serializers.SerializerMethodField()
    user_name = serializers.SerializerMethodField()
    science_name = serializers.SerializerMethodField()

    class Meta:
        model = Result
        fields = ['id', 'user_phone', 'user_name', 'science_name', 'userball', 'maxball', 'created_at']

    def get_user_phone(self, obj):
        return obj.user.phone

    def get_user_name(self, obj):
        return obj.user.username

    def get_science_name(self, obj):
        science = getattr(obj, 'science', None)
        return getattr(science, 'name', '')
