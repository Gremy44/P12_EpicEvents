from django.contrib import admin

from authentication.models import User
from models.contract import Contract
from models.event import Event
from models.status import Status

from epicevents.permissions import Permissions


class ContractAdmin(Permissions, admin.ModelAdmin):
        
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'sales_contact':  # Nom du champ ForeignKey à filtrer
            # Appliquer un filtre sur le champ 'sales_contact' en utilisant un queryset
            kwargs['queryset'] = User.objects.filter(role='VT') # Remplacez 'VENDEURS' par le nom de votre groupe

        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
    fields = ('client', 'amount', 'payment_due', 'sales_contact', 'status')
    exclude = ['date_created', 'date_updated']
    
class EventAdmin(Permissions, admin.ModelAdmin):
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'support_contact':  # Nom du champ ForeignKey à filtrer
            # Appliquer un filtre sur le champ 'sales_contact' en utilisant un queryset
            kwargs['queryset'] = User.objects.filter(role='SP') # Remplacez 'VENDEURS' par le nom de votre groupe

        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
class StatusAdmin(Permissions, admin.ModelAdmin):
    pass