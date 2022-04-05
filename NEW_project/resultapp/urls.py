from django.urls import path
from rest_auth.views import LogoutView
from .views import *


urlpatterns = [
    path('check-answers/', CheckAnswer.as_view()),
    path('my-results/', MyResultListView.as_view()),
    path('all-results/', StudentsResultList.as_view()),
    path('random/', ResultsCreate.as_view()),
    ]