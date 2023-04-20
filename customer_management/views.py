from django.shortcuts import render
from rest_framework import mixins, viewsets

from models.client import Client
from models.prospect import Prospect

from serializers.client import ClientSerializer
from serializers.prospect import ProspectSerializer


class ClientViewset(viewsets.GenericViewSet):
    
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

 
class ProspectViewset(viewsets.GenericViewSet,):
    
    queryset = Prospect.objects.all()
    serializer_class = ProspectSerializer
