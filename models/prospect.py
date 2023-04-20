from django.db import models
from django.conf import settings


class Prospect(models.Model):
    
    class Meta:
        app_label="customer_management"
        
    company_name = models.CharField(max_length=25)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    notes = models.TextField()
    sales_contact = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    
    def __str__(self) -> str:
        return self.company_name