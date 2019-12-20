from django.contrib import admin
from django.urls import path,include
from .views import *
from rest_framework_simplejwt import views as jwt_views

urlpatterns=[
	path('',HomeView,name='home'),
	path('signup',CreateCompanyView.as_view(),name='signup_company'),	
	path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]