from rest_framework import serializers
from .models import Order


class order_serializer(serializers.ModelSerializer) :
    total = serializers.SerializerMethodField()
    class Meta :
        model = Order
        fields = [ "cartitems","order_id","created_at","total"]
    def get_total(self, obj):
        return sum(item.product.product_price * item.quantity for item in obj.cartitems.all())