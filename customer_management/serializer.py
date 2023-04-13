from django.utils import timezone
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import serializers
# from django.contrib.auth.models import User
from customer_management.models import Client, Prospect
from authentication.models import User

class ClientSerializer(serializers.ModelSerializer):
    sales_contact = serializers.PrimaryKeyRelatedField(queryset=get_user_model().objects.all())

    class Meta:
        model = Client
        fields = ['id', 'id_prospect', 'company_name', 'first_name', 'last_name', 'email', 'phone', 'mobile',
                  'sales_contact', 'date_created', 'date_updated']
        read_only_fields = ['id', 'date_created', 'date_updated']

    def create(self, validated_data):
        id_prospect = validated_data.get('id_prospect')
        company_name = validated_data['company_name']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        email = validated_data['email']
        phone = validated_data['phone']
        mobile = validated_data['mobile']
        sales_contact = validated_data['sales_contact']

        sales_contact = get_user_model().objects.get(id=sales_contact.id)

        client = Client(
            company_name=company_name,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            mobile=mobile,
            sales_contact=sales_contact,
        )

        if id_prospect:
            client.id_prospect = Prospect.objects.get(id=id_prospect.id)
            
        client.save()
        return client

    def update(self, instance, validated_data):
        instance.id_prospect = validated_data.get('id_prospect', instance.id_prospect)
        instance.company_name = validated_data.get('company_name', instance.company_name)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.mobile = validated_data.get('mobile', instance.mobile)
        instance.sales_contact = validated_data.get('sales_contact', instance.sales_contact)
        instance.save()
        return instance
    
    
from rest_framework import serializers
from .models import Prospect
from django.contrib.auth import get_user_model

class ProspectSerializer(serializers.ModelSerializer):
    
    sales_contact = serializers.PrimaryKeyRelatedField(queryset=get_user_model().objects.all(), allow_null=True)

    class Meta:
        model = Prospect
        fields = '__all__'
        read_only_fields = ['id', 'date_created', 'date_updated']

    def create(self, validated_data):
        sales_contact = get_user_model().objects.get(id=sales_contact.id)
        prospect = Prospect(
            company_name=validated_data['company_name'],
            email=validated_data['email'],
            phone=validated_data['phone'],
            notes=validated_data['notes'],
            sales_contact=sales_contact,
        )
        prospect.save()
        return prospect

    def update(self, instance, validated_data):
        instance.company_name = validated_data.get('company_name', instance.company_name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.notes = validated_data.get('notes', instance.notes)
        instance.sales_contact = validated_data.get('sales_contact', instance.sales_contact)
        instance.save()
        return instance