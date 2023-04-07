from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USER_STATUS = [
        ('VT', 'Vente'),
        ('SP', 'Support'),
        ('GT', 'Gestion'),
    ]
    
    class Meta:
        verbose_name_plural = "Staff"

    phone = models.CharField(max_length=20)
    role = models.CharField(max_length=2, choices=USER_STATUS)
    
    def __str__(self):
        return self.username
