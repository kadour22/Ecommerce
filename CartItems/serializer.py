from rest_framework import serializers
from .models import CartItems


class cartitems_serializer(serializers.ModelSerializer) :
    # total = serializers.SerializerMethodField()
    class Meta :
        model = CartItems
        fields = ['id','product', 'quantity', 'guest_id']
        extra_kwargs = {
            'guest_id': {'required': False, 'allow_null': True}
        }
    # def get_total(self, obj):
    #     return obj.product.product_price * obj.quantity