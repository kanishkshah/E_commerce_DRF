from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer):
	publisher = serializers.PrimaryKeyRelatedField(
		read_only=True, 
		default=serializers.CurrentUserDefault()
	)
	class Meta:
		model=Product
		fields=('descrip','title','image','cost','publisher')

class CartSerializer(serializers.ModelSerializer):
	# user = serializers.PrimaryKeyRelatedField(
	# 	read_only=True, 
	# 	default=serializers.CurrentUserDefault()
	# ) 

	# After a bit of experimentation, Django actually treats the user 
	# and Publisher fieldnames slightly differently. Maybe because 
	# Product publisher is a Foreign Key and cart user is a OnetoOneField.
	# Huh.?
	class Meta:
		model=Cart
		fields=('products','user')