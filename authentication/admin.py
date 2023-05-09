from django.contrib.auth.models import Permission
from django.contrib import admin
from django.apps import apps
from django import forms

from authentication.models import User

from epicevents.permissions import Permissions

from customer_management.admin import (Client,
                                       ClientAdmin,
                                       Prospect,
                                       ProspectAdmin)

from event_management.admin import (Contract,
                                    ContractAdmin,
                                    Event,
                                    EventAdmin,
                                    Status,
                                    StatusAdmin)


class MyAdmin(admin.AdminSite):
    
    site_header = "EpicEvent Administration"
    site_title = "EpicEvent"
    final_catch_all_view = False


class UserAdminForm(Permissions, forms.ModelForm):
    
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'role', 'email', 'phone']  # Spécifier les champs à inclure dans le formulaire
        exclude = ['last_login', 'is_superuser', 'date_joined', 'user_permissions']


class UserAdmin(Permissions, admin.ModelAdmin):
    
    form = UserAdminForm
    
    list_display = ['first_name', 'last_name', 'username', 'email', 'role', 'phone']


admin_site = MyAdmin(name="admin")

admin_site.register(User, UserAdmin)
admin_site.register(Client, ClientAdmin)
admin_site.register(Prospect, ProspectAdmin)
admin_site.register(Contract, ContractAdmin)
admin_site.register(Event, EventAdmin)
admin_site.register(Status, StatusAdmin)
