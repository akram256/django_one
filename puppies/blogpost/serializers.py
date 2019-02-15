from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from blogpost.models import Puppy


class PuppySerializer(serializers.ModelSerializer):
    class Meta:
        model = Puppy
        fields =('name','age','breed','color','created_at','updated_at')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =('username','email','password')
        extra_kwargs = {'password':{'write_only': True}}