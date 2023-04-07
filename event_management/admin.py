from django.contrib import admin

from event_management.models import Contract, Event, Status

@admin.register(Contract, Event, Status)
class GenericAdmin(admin.ModelAdmin):
    pass

