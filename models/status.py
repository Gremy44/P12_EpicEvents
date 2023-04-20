from django.db import models
from django.conf import settings


class Status(models.Model):
    
    class Meta:
        verbose_name_plural = "Status"
        app_label="event_management"

    name = models.CharField(max_length=25)
    
    def __str__(self) -> str:
        return str(self.name)
