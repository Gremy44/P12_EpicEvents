from django.contrib import admin

from authentication.models import User

@admin.register(User)
class GenericAdmin(admin.ModelAdmin):
    
    list_display = ['first_name', 'last_name', 'username', 'email', 'phone', 'role']
    exclude = ['last_login', 'is_superuser', 'date_joined', 'user_permissions']