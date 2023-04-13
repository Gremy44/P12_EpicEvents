from django.contrib.auth.models import AbstractUser
from django.db import models

from django.contrib.auth.hashers import make_password
from django.db.models.signals import pre_save
from django.dispatch import receiver


class User(AbstractUser):
    USER_STATUS = [
        ('VT', 'Vente'),
        ('SP', 'Support'),
        ('GT', 'Gestion'),
    ]
    
    class Meta:
        verbose_name_plural = "Staff"

    phone = models.CharField(blank=True, max_length=20)
    role = models.CharField(max_length=7, choices=USER_STATUS, default='VT')
    is_staff = models.BooleanField(default=True, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')
    
    def set_password(self, password):
        """
        Méthode pour définir le mot de passe de l'utilisateur de manière sécurisée.
        """
        self.password = make_password(password)

    def __str__(self):
        return self.username
    