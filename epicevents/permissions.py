from rest_framework.permissions import BasePermission, IsAuthenticated
import json


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
    
    def request_permissions_set(self, request):
        
        print('IS_STAFF : ', request.user.is_staff)
        
        request_type = request.method
        user_role = self.role_translate(request.user.role)
        try :
            model_request = request.path.split('/')[3].title()
        except IndexError:
            model_request = None
        jsondata = self.json_loader('epicevents\permissions_set.json')
        
        for role in jsondata:
            if role == user_role:
                for model in jsondata[role]:
                    if model == model_request:
                        for in_request in jsondata[role][model]:
                            if in_request == request_type:
                                print(f'{role}|{user_role} --- {model}|{model_request} --- {in_request}|{request_type}')
                                return jsondata[role][model][in_request]
        print('DAMN NOOO')
        if request.user.is_staff:
            return True
        return False
    
    def has_view_permission(self, request, obj=None):
        print(request.user.is_staff)
        if request.user.is_staff:
            return True
        
    def has_add_permission(self, request, obj=None):
        print(request.user.is_staff)
        if request.user.is_staff:
            return True
        return self.request_permissions_set(request)

    def has_change_permission(self, request, obj=None):
        print(request.user.is_staff)
        if request.user.is_staff:
            return True
        return self.request_permissions_set(request)

    def has_delete_permission(self, request, obj=None):
        print(request.user.is_staff)
        if request.user.is_staff:
            return True
        return self.request_permissions_set(request)


class CustomPermission():
    def has_view_permission(self, request, obj=None):
        print(request.user.is_staff)
        if request.user.is_staff:
            return True