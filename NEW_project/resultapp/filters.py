from django_filters import rest_framework as filters
from . models import *


class ResultFilter(filters.FilterSet):
    class Meta:
        model = Result
        fields = ['science']