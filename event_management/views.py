from rest_framework import mixins, viewsets

from models.event import Event
from models.contract import Contract
from models.status import Status

from serializers.event import EventSerializer
from serializers.contract import ContractSerializer
from serializers.status import StatusSerializer

from epicevents.permissions import Permissions_API


class EventViewset(viewsets.ModelViewSet):
    
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [Permissions_API]


class ContractViewset(Permissions_API, viewsets.ModelViewSet):
    
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [Permissions_API]


class StatusViewset(Permissions_API, viewsets.ModelViewSet):
    
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [Permissions_API]
