from rest_framework.permissions import BasePermission
from authentication.models import User


permissions_set = {
    'User':
        {
            'GET': True,
            'POST': False,
            'UPDATE': False,
            'DELETE': False,
        },
    'Prospect':
        {
            'GET': False,
            'POST': False,
            'UPDATE': False,
            'DELETE': False,
        },
    'Client':
        {
            'GET': False,
            'POST': False,
            'UPDATE': False,
            'DELETE': False,
        },
    'Contract':
        {
            'GET': False,
            'POST': False,
            'UPDATE': False,
            'DELETE': False,
        },
    'Event':
        {
            'GET': False,
            'POST': False,
            'UPDATE': False,
            'DELETE': False,
        },
}

class Mixin_Permissions():
    
    def Mixin_Permissions(self):
        print('ROLE : ', self.request.user.role)
        if self.request.user.is_authenticated:
            if self.request.user.role == 'VT':
                permissions = [Is_Sale()]
            elif self.request.user.role == 'SP':
                permissions = [Is_Support()]
            elif self.request.user.role == 'GT':
                permissions = [Is_Gestion()]
            else:
                permissions = []
        else:
            permissions = []
        return permissions

# request.method
# view.queryset.model.__name__
class Is_Gestion(BasePermission):
    '''def has_permission(self, request, view):
        for model in permissions_set:
            if model == view.queryset.model.__name__:
                for request_method in permissions_set[model]:
                    if request_method == request.method:
                        return permissions_set[model][request_method]

    
    def has_object_permission(self, request, view, obj):
        for model in permissions_set:
            if model == view.queryset.model.__name__:
                for request_method in permissions_set[model]:
                    if request_method == request.method:
                        return permissions_set[model][request_method]'''
    
    def has_permission(self, request, view):
        return True

    
    def has_object_permission(self, request, view, obj):
        return True
    

class Is_Sale(BasePermission):
    def has_permission(self, request, view):
        return True
        
    
    def has_object_permission(self, request, view, obj):
        return True


class Is_Support(BasePermission):
    def has_permission(self, request, view):
        return True
    
    def has_object_permission(self, request, view, obj):
        return True