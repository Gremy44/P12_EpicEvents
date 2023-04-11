from django.contrib import admin
from django.contrib.auth.models import Group
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple

from authentication.models import User


class UserAdminForm(forms.ModelForm):
    
    groupes = Group.objects.all()

    GROUPE_CHOICES = (
        ('3', 'Gestion'),
        ('1', 'Sale'),
        ('2', 'Support'),
    )
    
    groups = forms.ChoiceField(choices=GROUPE_CHOICES)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'groups', 'email', 'phone']  # Spécifier les champs à inclure dans le formulaire
        exclude = ['last_login', 'is_superuser', 'date_joined', 'user_permissions']
        widgets = {
            'groups': forms.RadioSelect,  # Utiliser le widget CheckboxSelectMultiple pour le champ ManyToManyField 'groups'
        }

class UserAdmin(admin.ModelAdmin):
    
    form = UserAdminForm
    
    list_display = ['first_name', 'last_name', 'username', 'email', 'phone']
    
    
    
admin.site.register(User, UserAdmin)
