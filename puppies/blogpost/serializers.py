from rest_framework import serializers
from blogpost.models import Puppy


class PuppySerializer(serializers.ModelSerializer):
    class Meta:
        model = Puppy
        fields =('name','age','breed','color','created_at','updated_at')