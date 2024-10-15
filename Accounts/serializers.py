from rest_framework import serializers

from Accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','phone_number','full_name','password']

