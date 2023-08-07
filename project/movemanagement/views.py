from rest_framework import viewsets
from .serializers import *
from .models import *
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework import generics
from rest_framework.authentication import  TokenAuthentication
from rest_framework.response import Response
from knox.auth import AuthToken
from rest_framework.views import APIView
from rest_framework import status

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
            print("successfully loged in")
            return Response({
                "user": UserSerializer(user, context=self.get_serializer_context()).data,
                "token": AuthToken.objects.create(user)[1]
            })

class ResetPassword(APIView):
        def post(self,request):
                serializer=ResetPasswordSerializer(data=request.data)
                alldatas={}
                if serializer.is_valid(raise_exception=True):
                        serializer.save()
                        alldatas['data']="successfully registered"
                        print(alldatas)
                        return Response(alldatas)
                else:
                    return Response("failed retry after some time")


#project names views
class ProjectView(viewsets.ModelViewSet):
        method='GET'
        # authentication_classes= [TokenAuthentication]
        # permission_classes=(IsAuthenticated,) 
        queryset=Project.objects.all()
        serializer_class=ProjectSerializer

#project users view
class ProjectUserView(viewsets.ModelViewSet):
        method='GET'
        # authentication_classes= [TokenAuthentication]
        # permission_classes=(IsAuthenticated,)   
        queryset=ProjectUser.objects.all()
        serializer_class=ProjectUserSerializer

#documentation view
class DocumentationView(viewsets.ModelViewSet):
    method='GET'
    # authentication_classes= [TokenAuthentication]
    # permission_classes=(IsAuthenticated)
    queryset=Documentation.objects.all()
    serializer_class=DocumentationSerializer

#users documentation view
class UserView(viewsets.ModelViewSet):
        method='GET'
        # authentication_classes= [TokenAuthentication]
        # permission_classes=(IsAuthenticated)
        queryset=User.objects.all()
      
class Count(APIView):
       def get(self):
              projectcount=Project.objects.count()
              ProjectUsercount=ProjectUser.objects.count()
              Documentationcount=Documentation.objects.count()
              return Response({
                "project_count": projectcount,
                "ProjectUsercount": ProjectUsercount,
                "Documentationcount": Documentationcount,
         
            })
              