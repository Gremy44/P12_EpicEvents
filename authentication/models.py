from django.contrib.auth.models import AbstractUser
from django.db import models

from django.contrib.auth.hashers import make_password


class User(AbstractUser):
    USER_STATUS = [
        ('VT', 'Vente'),
        ('SP', 'Support'),
        ('GT', 'Gestion'),
    ]
    
    class Meta:
        verbose_name_plural = "Staff"
        app_label = "authentication"

    phone = models.CharField(blank=True, max_length=20)
    role = models.CharField(max_length=7, choices=USER_STATUS, default='VT')
    is_staff = models.BooleanField(default=True, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')
    
    def save(self, *args, **kwargs):
        # Appeler set_password avant d'enregistrer l'utilisateur
        if self.password and not self.password.startswith('pbkdf2_'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username