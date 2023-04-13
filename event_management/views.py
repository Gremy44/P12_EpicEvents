from django.shortcuts import render
from rest_framework import generics, mixins, viewsets

from event_management.models import Event, Contract, Status
from event_management.serializer import EventSerializer, ContractSerializer, StatusSerializer

from epicevents.permissions import Mixin_Permissions


class EventViewset(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet,
                    Mixin_Permissions):
    
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class ContractViewset(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet,
                    Mixin_Permissions):
    
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer


class StatusViewset(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet,
                    Mixin_Permissions):
    
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
