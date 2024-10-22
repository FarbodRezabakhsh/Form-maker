from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from Accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','phone_number','full_name','password']


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password],required=True)
    password2 = serializers.CharField(write_only=True,required=True)

    class Meta:
        model = User
        fields = ['email','phone_number','full_name','password','password2']

    def create(self,validated_data):
        del validated_data['password2']
        return User.objects.create_user(**validated_data)

    def validate_email(self,value):
        if 'admin' in value.lower():
            raise serializers.ValidationError('Email should not include admin word')
        return value

    def validate(self,data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({'password':'password fields did not match'})
        return data
