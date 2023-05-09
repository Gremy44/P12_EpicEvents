from django.contrib.auth.models import Permission
from rest_framework.permissions import BasePermission
import json

from models.event import Event
from models.contract import Contract
from models.status import Status
from models.client import Client
from models.prospect import Prospect


class Permissions():

    def role_translate(self, role):
        if role == 'SP':
            role = 'Support'
        elif role == 'VT':
            role = 'Vente'
        else:
            role = 'Gestion'
        return role

    def json_loader(self, file):
        with open(file, 'r') as f:
                data = json.load(f)
                return data
    
    def request_permissions_set(self, request, request_type):

        user_role = self.role_translate(request.user.role)
        try :
            model_request = request.path.split('/')[3].title()
        except IndexError:
            model_request = None
        jsondata = self.json_loader('epicevents\permissions_set.json')
        
        url = request.get_full_path()
        url_parts = url.split("/")
        last_part = url_parts[-1]
        
        for role in jsondata:
            if role == user_role:
                for model in jsondata[role]:
                    if model == model_request:
                        for in_request in jsondata[role][model]:
                            if in_request == request_type:
                                # print(f'{role}|{user_role} --- {model}|{model_request} --- {in_request}|{request_type}')
                                return jsondata[role][model][in_request]
        return False
    
    def has_view_permission(self, request, obj=None):
        # print("1")
        # method = 'GET'
        # permission = self.request_permissions_set(request, method)
        # print('PERMISSIONS POST: ', permission)
        return True
        
    def has_add_permission(self, request, obj=None):
        # print("2")
        method = 'POST'
        permission = self.request_permissions_set(request, method)
        # print('PERMISSIONS POST: ', permission)
        return permission

    def has_change_permission(self, request, obj=None):
        # print("3")
        method = 'UPDATE'
        permission = self.request_permissions_set(request, method)
        # print('PERMISSIONS UPDATE: ', permission)
        return permission

    def has_delete_permission(self, request, obj=None):
        # print("4")
        method = 'DELETE'
        permission = self.request_permissions_set(request, method)
        # print('PERMISSIONS DELETE: ', permission)
        return permission


class Permissions_API(BasePermission):
    perm = Permissions()
    
    def has_permission(self, request, view):
        method = request.method
        permission = self.perm.request_permissions_set(request, method)
        print(f'REQUEST : type: {method} --- permissions: {permission}')
        return permission

    def has_object_permission(self, request, view, obj):
        method = request.method
        permission = self.perm.request_permissions_set(request, method)
        print(f'REQUEST : type: {method} --- permissions: {permission}')
        return permission