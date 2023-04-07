from django.contrib import admin
from django import forms
from django.shortcuts import render
from django.urls import reverse

from customer_management.models import Client, Prospect

        
class ClientAdmin(admin.ModelAdmin):
    # Liste des champs que vous souhaitez afficher dans l'administration
    fields = [
                    'id_prospect', 
                    'company_name',
                    'first_name',
                    'last_name',
                    'email',
                    'phone',
                    'mobile',
                    'sales_contact',
                    ]


admin.site.register(Client, ClientAdmin)  
admin.site.register(Prospect)  
    