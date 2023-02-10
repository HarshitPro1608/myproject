
from rest_framework import serializers
from .models import Client, Artist, Work
from django.contrib.auth.models import User
from rest_framework import generics
# from rest_framework.parsers import JSONParser

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'

class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

