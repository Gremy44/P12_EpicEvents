from django.db import models
from django.conf import settings

from models.prospect import Prospect


class Client(models.Model):
    
    class Meta:
        app_label="customer_management"
    
    prospect = models.ForeignKey(Prospect, on_delete=models.CASCADE, null=True, blank=True)
    company_name = models.CharField(max_length=25)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    mobile = models.CharField(max_length=20)
    sales_contact = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.company_name