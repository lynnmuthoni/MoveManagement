from imaplib import _Authenticator
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from movemanagement.models import *
from django.contrib.auth import authenticate

## login
class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
             return user
        raise serializers.ValidationError("Invalid Details.")
    
##signup serializercd 
class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ["id","username"]

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
    required=True,
    allow_blank=False,
    validators=[UniqueValidator(queryset=User.objects.all())]
    ) 
    # firstname=serializers.CharField(
    #     required=True,
    #     validators=[UniqueValidator(queryset=User.objects.all())]
    # )
    password = serializers.CharField(
    write_only=True, required=True, validators=[validate_password])
    # password2 = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        fields = ('username','password',
             'email',)
        
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
          raise serializers.ValidationError(
            {"password": "Password fields didn't match."})
        return attrs
    def create(self, validated_data):
        user = User.objects.create(
          username=validated_data['username'],
          email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
## details serializers
class ProjectUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProjectUser
        fields=('id','username','password')

class DocumentationSerializer(serializers.ModelSerializer):
    class Meta:
        model= Documentation
        fields=('id','projectname','description','documentation')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields=('id','Projectname','date','url','projectuser','documentation')
        depth=1
