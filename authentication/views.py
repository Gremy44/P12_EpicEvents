from django.shortcuts import render

from rest_framework import generics, viewsets, mixins
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

from authentication.models import User
from authentication.serializer import UserSerializer

from epicevents.permissions import Mixin_Permissions

class ActualUserView(Mixin_Permissions, ReadOnlyModelViewSet):

    serializer_class = UserSerializer

    def get_queryset(self):
        user = User.objects.filter(id=self.request.user.id)
        return user
    

class UserViewset(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet,
                  Mixin_Permissions):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
