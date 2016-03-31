from datetime import datetime

from django.contrib.auth import update_session_auth_hash

from rest_framework import serializers

from authentication.models import Account
from authentication.services import calculate_age


# ----------------- #
# AccountSerializer #
# ----------------- #

class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False, label='Mot de passe')
    confirm_password = serializers.CharField(write_only=True, required=False, label='Confirmer le mot de passe.')
    
    class Meta:
        model = Account
        fields = (
            'id', 'email', 'username', 'date_of_birth', 'first_name',
            'last_name', 'delivery_adress', 'delivery_adress_complement',
            'delivery_zip_code', 'delivery_town', 'billing_adress',
            'billing_adress_complement','billing_zip_code', 'billing_town',
            'phone_number', 'tagline', 'password', 'confirm_password',
            'is_admin', 'is_active', 'created_at', 'updated_at'
        )
    
    def validate_date_of_birth(self, value):
        born = datetime.strptime(value, '%Y-%m-%d')
        
        if calculate_age(born) < 13:
            raise serializers.ValidationError('Vous devez avoir 13 ans minimum pour vous inscrire.')
        
        return value
    
    def create(self, validated_data):
        return Account.objects.create(**validated_data)
        
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.tagline = validated_data.get('tagline', instance.tagline)
    
        instance.save()
        
        password = validated_data.get('password', None)
        confirm_password = validated_data.get('confirm_password', None)
        
        if password and confirm_password and password == confirm_password:
            instance.set_password(password)
            instance.save()
        
        update_session_auth_hash(self.context.get('request'), instance)
        
        return instance
