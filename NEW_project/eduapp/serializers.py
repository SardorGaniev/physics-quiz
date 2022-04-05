from rest_framework import serializers
from . import models


# Предметы
class ScienceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Science
        fields = '__all__'


# Тесты
class QuestionListSerializer(serializers.ModelSerializer):
    science_name = serializers.SerializerMethodField()

    class Meta:
        model = models.Question
        fields = '__all__'

    def get_science_name(self, obj):
        science = getattr(obj, 'science', None)
        return getattr(science, 'name', '')
