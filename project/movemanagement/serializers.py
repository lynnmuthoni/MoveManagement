from pyexpat.errors import messages
from rest_framework import serializers
from django.contrib.auth.models import User,auth
from rest_framework import exceptions
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .models import *
from django.contrib.auth import authenticate

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
class ResetPasswordSerializer(serializers.Serializer):
    username=serializers.CharField(max_length=100,required=True)
    password=serializers.CharField(max_length=100,required=True)
    class Meta:
        model=User
        fields=('username','password')
    def save(self):
        username=self.validated_data['username']
        password=self.validated_data['password']
        #filtering out whethere username is existing or not, if your username is existing then if condition will allow your username
        if User.objects.filter(username=username).exists():
            #if your username is existing get the query of your specific username 
            user=User.objects.get(username=username)
            #then set the new password for your username
            user.set_password(password)
            user.save()
            return user
        else:
            raise serializers.ValidationError({'error':'please enter valid crendentials'})

##user serializercd 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","username","password"]

    
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

        