"""epicevents URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework import routers
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,\
    TokenRefreshView

from authentication.views import ActualUserView, UserViewset
from customer_management.views import ClientViewset, ProspectViewset
from event_management.views import EventViewset, ContractViewset, StatusViewset

from authentication.admin import admin_site


router = routers.DefaultRouter()

# Vue pour l'utilisateur actuel
router.register(r'api/actual-user', ActualUserView, basename='actual-user')

# Vues pour les utilisateurs
router.register(r'api/authentication/user', UserViewset, basename='user')
# Vues pour les clients
router.register(r'api/customer-management/client', ClientViewset, basename='client')
# Vues pour les prospects
router.register(r'api/customer-management/prospect', ProspectViewset, basename='prospect')
# Vues pour les événements
router.register(r'api/event-management/event', EventViewset, basename='event')
# Vues pour les contrats
router.register(r'api/event-management/contract', ContractViewset, basename='contract')
# Vues pour les statuts
router.register(r'api/event-management/status', StatusViewset, basename='status')


urlpatterns = [
    path('admin/', admin_site.urls),
    path(r'api/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(r'api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + router.urls
