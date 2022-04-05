from rest_framework import views, status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings
from .models import *
from . import serializers
from helpapp.paginations import *

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

# Регистрация
class UserReg(views.APIView):
    def post(self, request, *args, **kwargs):
        phone = request.data.get('phone', None)
        fullname = request.data.get('fullname', None)
        password = request.data.get('password', None)
        password2 = request.data.get('password2', None)
        if (phone is None) or (password is None):
            return Response({
                'status': False,
                'detail': "phone and password require"
            }, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.filter(phone=phone).first()
        if not (user is None):
            return Response({
                'status': False,
                'detail': "user not found"
            }, status=status.HTTP_400_BAD_REQUEST)
        if len(phone) != 12:
            return Response({
                'status': False,
                'detail': "error phone"
            }, status=status.HTTP_400_BAD_REQUEST)
        if len(password) >= 8 and password != password2:
            return Response({
                'status': False,
                'detail': "error password"
            }, status=status.HTTP_400_BAD_REQUEST)
        userObj = User.objects.create_user(phone=phone, password=password, username=fullname)
        payload = jwt_payload_handler(userObj)
        token = jwt_encode_handler(payload)

        return Response({
            'id': userObj.id,
            'token': token,
            'fullname': userObj.username,
            'phone': userObj.phone,
            'status': True
        })

# Моя страница
class MyPaige(generics.ListAPIView):
    def get_queryset(self):
        user = self.request.user.phone
        queryset = User.objects.filter(phone=user)
        return queryset
    queryset = User.objects.all
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.StudentPaigeSerializer
