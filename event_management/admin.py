from django.contrib import admin

from event_management.models import Contract, Event, Status
from authentication.models import User


class ContractAdmin(admin.ModelAdmin):
        
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'sales_contact':  # Nom du champ ForeignKey à filtrer
            # Appliquer un filtre sur le champ 'sales_contact' en utilisant un queryset
            kwargs['queryset'] = User.objects.filter(groups__name='Sale') # Remplacez 'VENDEURS' par le nom de votre groupe

        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
    fields = ('client', 'amount', 'payment_due', 'sales_contact', 'status')
    exclude = ['date_created', 'date_updated']
    
class EventAdmin(admin.ModelAdmin):
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'support_contact':  # Nom du champ ForeignKey à filtrer
            # Appliquer un filtre sur le champ 'sales_contact' en utilisant un queryset
            kwargs['queryset'] = User.objects.filter(groups__name='Support') # Remplacez 'VENDEURS' par le nom de votre groupe

        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
admin.site.register(Contract, ContractAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Status)