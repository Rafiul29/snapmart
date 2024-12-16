from rest_framework import serializers
from .models import UserAccount
import re

class UserAccountRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = UserAccount
        fields = ['username', 'first_name', 'last_name', 'email', 'role', 'password', 'confirm_password']
       

    def save(self, **kwargs):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']

        if password != confirm_password:
            raise serializers.ValidationError({'password': "Password don't match."})
        
        if not re.match(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*()-+]).{8,}$', password):
            raise serializers.ValidationError({"password":"This password must contain at least 8 characters, one uppercase letter, one lowercase letter, one digit and one symbol."})

        if UserAccount.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': "Email already exists."})

        user = UserAccount.objects.create_user(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name
        )
        user.set_password(password)
        user.save()
        return user


class UserAccountLoginSerializer(serializers.Serializer):
  username = serializers.CharField(required = True)
  password = serializers.CharField(required = True)