from rest_framework import serializers
from .models import Product

class product_serializer(serializers.ModelSerializer):
    class Meta :
        model  = Product
        fields = ['product_name','product_price','product_image','descriptions','in_stock', 'category']

        