from rest_framework import viewsets
from .serializers import *
from .models import *
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework import generics
from rest_framework.authentication import  TokenAuthentication
from rest_framework.response import Response
from knox.auth import AuthToken
# signup view
class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer
  
#login view

class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


#project names views

class ProjectView(viewsets.ModelViewSet):
    # authentication_classes= [TokenAuthentication]
    # permission_classes=(IsAuthenticated,) 
    queryset=Project.objects.all()
    serializer_class=ProjectSerializer

#project users view
class ProjectUserView(viewsets.ModelViewSet):
    # authentication_classes= [TokenAuthentication]
    # permission_classes=(IsAuthenticated,)       
    queryset=ProjectUser.objects.all()
    serializer_class=ProjectUserSerializer
#documentation view
class DocumentationView(viewsets.ModelViewSet):
    # authentication_classes= [TokenAuthentication]
    # permission_classes=(IsAuthenticated)
    queryset=Documentation.objects.all()
    serializer_class=DocumentationSerializer

#users documentation view
class UserView(viewsets.ModelViewSet):
    # authentication_classes= [TokenAuthentication]
    # permission_classes=(IsAuthenticated)
    queryset=User.objects.all()
    serializer_class=UserSerializer