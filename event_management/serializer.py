from rest_framework import serializers
from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User
from event_management.models import Event, Contract, Status
from customer_management.models import Client
from authentication.models import User

class EventSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())
    status = serializers.PrimaryKeyRelatedField(queryset=Status.objects.all())
    support_contact = serializers.PrimaryKeyRelatedField(queryset=get_user_model().objects.all())
    
    class Meta:
        model = Event
        fields = '__all__'
        read_only_fields = ['id', 'date_created', 'date_updated']
        
    def create(self, validated_data):
        event = Event(
            client=validated_data['client'],
            status=validated_data['status'],
            support_contact=validated_data['support_contact'],
            attentees=validated_data['attentees'],
            event_date=validated_data['event_date'],
            notes=validated_data['notes']
        )
        event.save()
        return event
    
    def update(self, instance, validated_data):
        instance.client = validated_data.get('client', instance.client)
        instance.status = validated_data.get('status', instance.status)
        instance.support_contact = validated_data.get('support_contact', instance.support_contact)
        instance.attentees = validated_data.get('attentees', instance.attentees)
        instance.event_date = validated_data.get('event_date', instance.event_date)
        instance.notes = validated_data.get('notes', instance.notes)
        instance.save()
        return instance

class ContractSerializer(serializers.Serializer):
    pass

class StatusSerializer(serializers.Serializer):
    pass