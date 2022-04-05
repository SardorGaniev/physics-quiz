from rest_framework import permissions
from .models import *


class IsTeacher(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_teacher

    def has_object_permission(self, request, view, obj):
        return request.user and request.user.is_teacher
