from pyexpat.errors import messages
from rest_framework import serializers
from django.contrib.auth.models import User,auth
from rest_framework import exceptions
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .models import *
from django.contrib.auth import authenticate

## login
class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
             return user
        elif user and user.is_anonymous:
            raise serializers.ValidationError("Enter correct username")
        elif user is None:
            raise serializers.ValidationError("user not found")
        elif user.password is None:
            raise serializers.ValidationError("Enter correct password")

## reset password serializer

##user serializercd 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","username","password"]
from rest_framework import serializers
from django.contrib.auth.models import User

class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

## registration serializer
class RegisterSerializer(serializers.ModelSerializer):
            username=serializers.CharField(
                required=True,
            allow_blank=False,
            validators=[UniqueValidator(queryset=User.objects.all())]

            )
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
                ## function to creation user creation fields
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
## documentation serializer
class DocumentationSerializer(serializers.ModelSerializer):
    class Meta:
        model= Documentation
        fields=('id','projectname','description','documentation')

## projects serializer
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields=('id','Projectname','date','url','projectuser','documentation')
        depth=1

        