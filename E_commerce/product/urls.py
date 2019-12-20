from django.contrib import admin
from django.urls import path,include
from .views import *
#from rest_framework_simplejwt import views as jwt_views
from rest_framework import routers

router=routers.DefaultRouter()
router.register('Products',ProductView)
router.register('Cart',CartView)

urlpatterns=[
	path('',include(router.urls)),
	
]