from django.urls import path
from rest_auth.views import LogoutView
from .views import *


urlpatterns = [
    path('reg/', UserReg.as_view()),
    path('my-paige/', MyPaige.as_view()),
    ]