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
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView,\
    TokenRefreshView

from authentication.views import ActualUserView, UserViewset
from customer_management.views import ClientViewset, ProspectViewset
from event_management.views import EventViewset, ContractViewset, StatusViewset

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/actual-user/', ActualUserView.as_view({'get': 'list'}), name='actual-user'),
    # --- USERS ---
    path('api/authentication/user/', UserViewset.as_view({'get': 'list'}), name='user-list'),
    path('api/authentication/user/add/', UserViewset.as_view({'post': 'create'}), name='user-create'),
    path('api/authentication/user/<int:pk>/', UserViewset.as_view({'get': 'retrieve'}), name='user-retrieve'),
    path('api/authentication/user/<int:pk>/change/', UserViewset.as_view({'patch': 'partial_update'}), name='user-update'),
    path('api/authentication/user/<int:pk>/delete/', UserViewset.as_view({'delete': 'destroy'}), name='user-delete'),
    # --- CLIENTS ---
    path('api/customer_management/client/', ClientViewset.as_view({'get': 'list'}), name='client-list'),
    path('api/customer_management/client/add/', ClientViewset.as_view({'post': 'create'}), name='client-create'),
    path('api/customer_management/client/<int:pk>/', ClientViewset.as_view({'get': 'retrieve'}), name='client-retrieve'),
    path('api/customer_management/client/<int:pk>/change/', ClientViewset.as_view({'patch': 'partial_update'}), name='client-update'),
    path('api/customer_management/client/<int:pk>/delete/', ClientViewset.as_view({'delete': 'destroy'}), name='client-delete'),
    # --- PROSPECTS ---
    path('api/customer_management/prospect/', ProspectViewset.as_view({'get': 'list'}), name='prospect-list'),
    path('api/customer_management/prospect/add/', ProspectViewset.as_view({'post': 'create'}), name='prospect-create'),
    path('api/customer_management/prospect/<int:pk>/', ProspectViewset.as_view({'get': 'retrieve'}), name='prospect-retrieve'),
    path('api/customer_management/prospect/<int:pk>/change/', ProspectViewset.as_view({'patch': 'partial_update'}), name='prospect-update'),
    path('api/customer_management/prospect/<int:pk>/delete/', ProspectViewset.as_view({'delete': 'destroy'}), name='prospect-delete'),
    # --- EVENTS ---
    path('api/event_management/event/', EventViewset.as_view({'get': 'list'}), name='event-list'),
    path('api/event_management/event/add/', EventViewset.as_view({'post': 'create'}), name='event-create'),
    path('api/event_management/event/<int:pk>/', EventViewset.as_view({'get': 'retrieve'}), name='event-retrieve'),
    path('api/event_management/event/<int:pk>/change/', EventViewset.as_view({'patch': 'partial_update'}), name='event-update'),
    path('api/event_management/event/<int:pk>/delete/', EventViewset.as_view({'delete': 'destroy'}), name='event-delete'),
    # --- CONTRACTS ---
    path('api/event_management/contract/', ContractViewset.as_view({'get': 'list'}), name='contract-list'),
    path('api/event_management/contract/add/', ContractViewset.as_view({'post': 'create'}), name='contract-create'),
    path('api/event_management/contract/<int:pk>/', ContractViewset.as_view({'get': 'retrieve'}), name='contract-retrieve'),
    path('api/event_management/contract/<int:pk>/change/', ContractViewset.as_view({'patch': 'partial_update'}), name='contract-update'),
    path('api/event_management/contract/<int:pk>/delete/', ContractViewset.as_view({'delete': 'destroy'}), name='contract-delete'),
    # --- STATUS ---
    path('api/event_management/status/', StatusViewset.as_view({'get': 'list'}), name='status-list'),
    path('api/event_management/status/add/', StatusViewset.as_view({'post': 'create'}), name='status-create'),
    path('api/event_management/status/<int:pk>/', StatusViewset.as_view({'get': 'retrieve'}), name='status-retrieve'),
    path('api/event_management/status/<int:pk>/change/', StatusViewset.as_view({'patch': 'partial_update'}), name='status-update'),
    path('api/event_management/status/<int:pk>/delete/', StatusViewset.as_view({'delete': 'destroy'}), name='status-delete'),
    
    path(r'api/auth/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path(r'api/auth/token/refresh/',
         TokenRefreshView.as_view(), name='token_refresh'),
]
