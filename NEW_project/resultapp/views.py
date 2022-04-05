from rest_framework import views
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import *
from .permissions import *
from . import serializers, filters
from userapp.models import User
from eduapp.models import Question, Science
from resultapp.models import Result
from helpapp.paginations import *
import random

# Получение ответов
class CheckAnswer(views.APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        answers = request.data['answers']
        slug = request.data['science']
        number_answers = len(answers)
        sum = 0
        for x in answers:
            model = Question.objects.all().filter(id=int(x['id']), slug=x['slug']).count()
            if model == 1:
                sum += 1
        science = Science.objects.filter(slug=slug).first()
        Result.objects.create(user=request.user, science=science, userball=sum, maxball=number_answers)
        return Response({
            'slug': slug,
            'userball': sum,
            'maxball': number_answers
        })

# Мои результаты
class MyResultListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        user = self.request.user
        queryset = Result.objects.filter(user=user)
        return queryset
    serializer_class = serializers.ResultSerializer
    filter_class = filters.ResultFilter

# Все результаты
class StudentsResultList(generics.ListAPIView):
    serializer_class = serializers.ResultSerializer
    filter_class = filters.ResultFilter
    queryset = Result.objects.all()
    search_fields = ['user__username']
    pagination_class = ListPagination
    # permission_classes = (IsTeacher,)

# Рандомные результаты
class ResultsCreate(views.APIView):
    def post(self, request, *args, **kwargs):
        for x in range(0,10):
            Result.objects.create(userball = random.randrange(1,4), maxball = random.randrange(5,10), user=User.objects.all().first(), science = Science.objects.all().first())
        return Response ({
            "status":"ok"
        })
    serializer_class = serializers.ResultSerializer
    # permission_classes = (IsAuthenticated,)

# print(Result)