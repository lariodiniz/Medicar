from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny

from access.serializers import UserCreateSerializer


class UserView(CreateAPIView):
    """create User View"""
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
