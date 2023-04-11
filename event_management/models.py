from django.db import models
from django.conf import settings

from customer_management.models import Client

class Status(models.Model):
    
    class Meta:
        verbose_name_plural = "Status"

    name = models.CharField(max_length=25)
    
    def __str__(self) -> str:
        return str(self.name)

class Contract(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False, verbose_name='Signed')
    amount = models.FloatField()
    payment_due = models.DateTimeField(auto_now_add=False)
    sales_contact = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return str(self.client)
    
class Event(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    support_contact = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    attentees = models.IntegerField()
    event_date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField()
    
    def __str__(self) -> str:
        return str(str(self.client) + ' --- ' + str(self.event_date))