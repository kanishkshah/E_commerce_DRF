from django.shortcuts import render
from rest_framework import viewsets
from .models import Product,Cart
from .serializers import ProductSerializer,CartSerializer
from django.core.exceptions import PermissionDenied

# Create your views here.

class ProductView(viewsets.ModelViewSet):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
	def perform_create(self, serializer):
		if(self.request.user.is_company):
			serializer.save(publisher=self.request.user)
		else:
			raise PermissionDenied()

class CartView(viewsets.ModelViewSet):
	queryset = Cart.objects.all()
	serializer_class = CartSerializer
	def perform_create(self, serializer):
		if(not self.request.user.is_company):
			serializer.save(user=self.request.user)
		else:
			raise PermissionDenied()