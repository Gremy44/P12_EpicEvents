from django.contrib import admin
from django.contrib.auth.models import Group
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple

from authentication.models import User


class UserAdminForm(forms.ModelForm):
    
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'role', 'email', 'phone']  # Spécifier les champs à inclure dans le formulaire
        exclude = ['last_login', 'is_superuser', 'date_joined', 'user_permissions']


class UserAdmin(admin.ModelAdmin):
    
    form = UserAdminForm
    
    list_display = ['first_name', 'last_name', 'username', 'email', 'phone']

   
admin.site.register(User, UserAdmin)
