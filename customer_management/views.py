from django.shortcuts import render
from rest_framework import mixins, viewsets

from models.client import Client
from models.prospect import Prospect

from serializers.client import ClientSerializer
from serializers.prospect import ProspectSerializer

from authentication.models import User
from epicevents.permissions import Permissions_API


class ClientViewset(Permissions_API, viewsets.ModelViewSet):
    
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [Permissions_API]

    
class ProspectViewset(Permissions_API, viewsets.ModelViewSet,):
    
    queryset = Prospect.objects.all()
    serializer_class = ProspectSerializer
    permission_classes = [Permissions_API]
