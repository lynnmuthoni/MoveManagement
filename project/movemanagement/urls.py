from django.urls import path,include
from .views import *
from rest_framework import routers
from .import views
from knox import views as knox_views
router=routers.DefaultRouter()
router.register('project',views.ProjectView)
router.register('projectuser',views.ProjectUserView)
router.register('documentations',views.DocumentationView)
router.register('users',views.UserView)
# router.register('count',views.Count,basename='Project')

urlpatterns = [
  path('',include(router.urls)),
  path('login/', LoginAPI.as_view()),
  path('logout/',knox_views.LogoutView.as_view()),
  path('count/', Count.as_view(), name='count'),
  path('register/',RegisterUserAPIView.as_view(),name='register'),
  path('resetpassword/',views.ResetPassword.as_view(),name='resetpassword'),
  
  
]

