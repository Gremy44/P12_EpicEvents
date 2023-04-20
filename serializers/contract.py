from rest_framework import serializers
from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User

from models.contract import Contract


class ContractSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contract
        fields = '__all__'
        app_label="event_management"

    def create(self, validated_data):
    # Récupérer les données validées
        client = validated_data.get('client')
        date_created = validated_data.get('date_created')
        date_updated = validated_data.get('date_updated')
        status = validated_data.get('status')
        amount = validated_data.get('amount')
        payment_due = validated_data.get('payment_due')
        sales_contact = validated_data.get('sales_contact')
        
        # Créer une nouvelle instance de Contract avec les données validées
        contract = Contract(
            client=client,
            date_created=date_created,
            date_updated=date_updated,
            status=status,
            amount=amount,
            payment_due=payment_due,
            sales_contact=sales_contact
        )
        
        # Sauvegarder l'instance dans la base de données
        contract.save()
        
        # Retourner l'instance créée
        return contract

    def update(self, instance, validated_data):
        instance.client = validated_data.get('client', instance.client)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.date_updated = validated_data.get('date_updated', instance.date_updated)
        instance.status = validated_data.get('status', instance.status)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.payment_due = validated_data.get('payment_due', instance.payment_due)
        instance.sales_contact = validated_data.get('sales_contact', instance.sales_contact)
        instance.save()
        return instance
