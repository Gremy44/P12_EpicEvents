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
    groups = models.ManyToManyField(help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')
    is_staff = models.BooleanField(default=True, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')
    
    def __str__(self):
        return self.username
    
@receiver(pre_save, sender=User)
def encrypt_password(sender, instance, **kwargs):
    """
    Signal handler to encrypt the password before saving the User instance.
    """
    instance.password = make_password(instance.password)
