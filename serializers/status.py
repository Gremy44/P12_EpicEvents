from rest_framework import serializers
from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User

from models.status import Status


class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = '__all__'
        app_label="event_management"

    def create(self, validated_data):
        status = Status(
            name=validated_data['name']
        )
        status.save()
        return status

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance