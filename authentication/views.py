from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Permission


from rest_framework import viewsets, mixins
from rest_framework.viewsets import ModelViewSet
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated


from authentication.models import User
from serializers.user import UserSerializer

from epicevents.permissions import Permissions_API


class ActualUserView(ReadOnlyModelViewSet):

    serializer_class = UserSerializer

    def get_queryset(self):
        user = User.objects.filter(id=self.request.user.id)
        return user
    

class UserViewset(ModelViewSet):
        
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [Permissions_API]
