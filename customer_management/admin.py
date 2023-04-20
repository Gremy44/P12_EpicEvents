from django.contrib import admin
from django.contrib import messages
from django.shortcuts import redirect

from authentication.models import User
from models.client import Client
from models.prospect import Prospect


@admin.action(description="Transform in client")
def make_client(Prospect, request, queryset):
    
    if request.method == 'POST' and len(queryset.values()) > 1: 
        messages.add_message(request, 30, "Select only on prospect to convert in client.")
    else:
        company_name = list(queryset.values_list('company_name', flat=True))[0]
        email = list(queryset.values_list('email', flat=True))[0]
        phone = list(queryset.values_list('phone', flat=True))[0]

        url_ajout_client = '/admin/customer_management/client/add/'  # Nom de la vue pour votre page d'ajout de client
        url_ajout_client += f'?company_name={company_name}&email={email}&phone={phone}'  # Ajout des paramètres de requête à l'URL
        
        return redirect(url_ajout_client)


class ProspectAdmin(admin.ModelAdmin):
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'sales_contact':  # Nom du champ ForeignKey à filtrer
            # Appliquer un filtre sur le champ 'sales_contact' en utilisant un queryset
            kwargs['queryset'] = User.objects.filter(role='VT') # Remplacez 'VENDEURS' par le nom de votre groupe

        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    actions = [make_client]
    
    
class ClientAdmin(admin.ModelAdmin):
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'sales_contact':  # Nom du champ ForeignKey à filtrer
            # Appliquer un filtre sur le champ 'sales_contact' en utilisant un queryset
            kwargs['queryset'] = User.objects.filter(role='VT') # Remplacez 'VENDEURS' par le nom de votre groupe

        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
    fields = [ 
                    'company_name',
                    ('first_name',
                    'last_name'),
                    'email',
                    ('phone',
                    'mobile'),
                    'sales_contact',
                    ]

    