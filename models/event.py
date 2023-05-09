from django.db import models
from django.conf import settings

from models.client import Client
from models.status import Status
from models.contract import Contract


class Event(models.Model):
    
    class Meta:
        app_label="event_management"

    event_name = models.CharField(max_length=40)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    support_contact = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    attentees = models.IntegerField()
    event_date = models.DateTimeField()
    notes = models.TextField()
    
    def __str__(self) -> str:
        return str(str(self.event_name) + ' --- ' + str(self.event_date))