from rest_framework import mixins, viewsets

from models.event import Event
from models.contract import Contract
from models.status import Status

from serializers.event import EventSerializer
from serializers.contract import ContractSerializer
from serializers.status import StatusSerializer


class EventViewset(viewsets.GenericViewSet,):
    
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class ContractViewset(viewsets.GenericViewSet):
    
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer


class StatusViewset(viewsets.GenericViewSet,):
    
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
