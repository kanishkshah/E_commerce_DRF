from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from .serializers import CompanySerializer
# Create your views here.

def HomeView(request,*args,**kwargs):
	return HttpResponse('Success')

class CreateCompanyView(CreateAPIView):

    model = get_user_model()
    permission_classes = [
        permissions.AllowAny 
    ]
    serializer_class = CompanySerializer