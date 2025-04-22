from django.forms import EmailField
from rest_framework import serializers
from .models import (
	Account,
)
from rest_framework.serializers import ValidationError

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            "first_name", "last_name", "username",
            "email", "date_of_birth", "gender",
            "account_role", "password"
        ]
        extra_kwargs = {
            "password": {"write_only": True}
        }

        
    def validate_email(self, value):
        if Account.objects.filter(email=value).exists():
            raise ValidationError("User with this email already exist.")
        return value.lower().strip()
    
    def create(self, validated_data):
        email = validated_data.pop("email", "")
        password = validated_data.pop("password", "")
        user = Account.objects.create_user(email=email, password=password, **validated_data)
        return user
    

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=50)
    
    def validate_email(self, value):
        return value.lower().strip()