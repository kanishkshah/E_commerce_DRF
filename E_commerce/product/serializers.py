from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model=Product
		fields=('descrip','title','image','cost')

class CartSerializer(serializers.ModelSerializer):
	class Meta:
		model=Cart
		fields=('products',)