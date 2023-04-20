from django.contrib.auth import get_user_model
from rest_framework import serializers
# from django.contrib.auth.models import User

from models.prospect import Prospect


class ProspectSerializer(serializers.ModelSerializer):
    
    sales_contact = serializers.PrimaryKeyRelatedField(queryset=get_user_model().objects.all(), allow_null=True)

    class Meta:
        model = Prospect
        fields = '__all__'
        read_only_fields = ['id', 'date_created', 'date_updated']
        app_label="customer_management"

    def create(self, validated_data):
        sales_contact = validated_data.get('sales_contact')
        if sales_contact:
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