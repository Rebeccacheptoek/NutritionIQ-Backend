from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import CustomUser


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'user_type', 'first_name', 'last_name', 'address', 'phone')

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            address=validated_data['address'],
            phone=validated_data['phone'],
            password=validated_data['password'],
            user_type=validated_data['user_type']
        )
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'})

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(email=email, password=password)
            if user:
                if not user.is_active:
                    raise serializers.ValidationError('User account is disabled.')
                attrs['user'] = user
            else:
                raise serializers.ValidationError('Unable to log in with the provided credentials.')
        else:
            raise serializers.ValidationError('Must include "email" and "password".')

        return attrs
