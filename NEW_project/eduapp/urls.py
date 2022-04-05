from django.urls import path
from . import views

urlpatterns = [
    path('science-list/', views.ScinenceListView.as_view()),
    path('question-list/<str:slug>', views.QuestionListView.as_view()),
    ]