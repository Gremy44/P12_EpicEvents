from django.contrib.auth.models import Group, Permission
from rest_framework.permissions import BasePermission
import json

from authentication.models import User


class NoAddChangeDeletePermissionMixin:
    def has_add_permission(self, request):
        return False  # Désactiver la permission d'ajout

    def has_change_permission(self, request, obj=None):
        return False  # Désactiver la permission de modification

    def has_delete_permission(self, request, obj=None):
        return False  # Désactiver la permission de suppression


class Request_Verification():
    def __init__(self, request, view):
        self.request = request
        self.view = view

    def json_recuperation_set(self):
        """Open and return 'permissions_set.json' 

        Args:
            None

        Returns:
            type: str()
        """
        with open('epicevents\permissions_set.json', 'r') as f:
            self.data = json.load(f)
            return self.data
            
    def retrieve_permissions(self, data):
        """Return the value in json file if request is allowed

        Args:
            data(json file): json file from json_recuperation_set()

        Returns:
            type: True or False
        """
        
        role_user = self.request.user.role
        my_request_type = self.request.method
        
        if role_user == 'SP':
            role_user = 'Support'
        elif role_user == 'VT':
            role_user = 'Vente'
        else:
            role_user = 'Gestion'

        for role in self.data:
            if role_user == role:
                for request_type in self.data[role]:
                    if self.data[role][request_type][my_request_type]:
                        print('Permissions set : True')
                        return True
                    print('Permissions set : False')
                    return False
                
    def get_role_and_request(self):
        """Return the value in json file if request is allowed
        Args:
            None
            
        Returns:
            type: tuple(role_user, my_request_type, model)
            Exemple : ('GT', 'GET', 'User')
        """
        role_user = self.request.user.role
        my_request_type = self.request.method
        model = self.view.queryset.model.__name__
        return (role_user, my_request_type, model)


class Choice_Permissions(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user.role == 'VT':
                permissions = [Is_Sale]
            elif request.user.role == 'SP':
                permissions = [Is_Support]
            elif request.user.role == 'GT':
                permissions = [Is_Gestion]
            else:
                permissions = []
        else:
            permissions = []
        return permissions

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)

class Is_Gestion(BasePermission):
    def has_permission(self, request, view):
        print('gestion')
        verif = Request_Verification(request, view)
        data = verif.json_recuperation_set()
        return verif.retrieve_permissions(data)

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)
    

class Is_Sale():
    def has_permission(self, request, view):
        print('vente')
        verif = Request_Verification(request, view)
        data = verif.json_recuperation_set()
        return verif.retrieve_permissions(data)

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)


class Is_Support(BasePermission):
    def has_permission(self, request, view):
        verif = Request_Verification(request, view)
        data = verif.json_recuperation_set()
        print('INFO : ', verif.get_role_and_request())
        return verif.retrieve_permissions(data)
    
    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)