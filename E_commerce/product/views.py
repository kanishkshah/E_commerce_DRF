from django.shortcuts import render
from rest_framework import viewsets
from .models import Product,Cart
from .serializers import ProductSerializer,CartSerializer
# Create your views here.

class ProductView(viewsets.ModelViewSet):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer

class CartView(viewsets.ModelViewSet):
	queryset = Cart.objects.all()
	serializer_class = CartSerializer