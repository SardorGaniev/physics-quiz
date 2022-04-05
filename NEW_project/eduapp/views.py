from django.shortcuts import render
from rest_framework import generics, views
from rest_framework.response import Response
from . import models, serializers
from rest_framework.permissions import IsAuthenticated
import random


class ScinenceListView(generics.ListAPIView):
    queryset = models.Science.objects.all()
    serializer_class = serializers.ScienceListSerializer
    permission_classes = [IsAuthenticated]


class QuestionListView(views.APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, slug, *args, **kwargs):
        qs = list(models.Question.objects.filter(science__slug=slug).values('id', 'name', 'slug', 'image'))
        science = models.Science.objects.filter(slug=slug).values('id', 'name', 'image', 'slug').first()
        ids = random.sample(qs, 4)
        imgs = random.sample(ids, 2)
        idsl = []
        for i in ids:
            idsl.append({'name': i['name'], 'slug': i['slug']})
        imgsl = []
        for i in imgs:
            imgsl.append({'image': i['image'], 'id': i['id']})
        return Response(
            {   'science': science,
                'slug': slug,
                'names': idsl,
                'images': imgsl
            }
        )
