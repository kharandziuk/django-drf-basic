import datetime

from rest_framework import serializers, viewsets

from django.utils.timezone import make_aware
from django.conf import settings

from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['username']

class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = UserSerializer
