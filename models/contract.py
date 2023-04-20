from django.db import models
from django.conf import settings

from models.client import Client


class Contract(models.Model):
    
    class Meta:
        app_label="event_management"

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False, verbose_name='Signed')
    amount = models.FloatField()
    payment_due = models.DateTimeField(auto_now_add=False)
    sales_contact = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return str(self.client)
