from django.shortcuts import render
from rest_framework import generics, mixins, viewsets

from customer_management.models import Client, Prospect
from customer_management.serializer import ClientSerializer, ProspectSerializer

from epicevents.permissions import Mixin_Permissions


class ClientViewset(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet,
                    Mixin_Permissions):
    
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

 
class ProspectViewset(mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet,
                      Mixin_Permissions):
    
    queryset = Prospect.objects.all()
    serializer_class = ProspectSerializer