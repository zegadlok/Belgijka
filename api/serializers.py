from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Room


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, data):
        user = User.objects.create_user(**data)
        Token.objects.create(user=user)
        return user


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model: Room
        fields = ('id', 'duration')
