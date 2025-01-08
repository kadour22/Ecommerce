from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from CartItems.models import CartItems
from Customer.models import Customer
from .models import Order
from .serializer import order_serializer
from django.core.mail import send_mail
from django.conf import settings

class passing_order_api_view(APIView):
    # Get the orders for the customers and guests and total-price of the orders
    def get(self, request , *args , **kwargs):
        guest_id = request.session.session_key
        orders = Order.objects.filter(cartitems__guest_id=guest_id).distinct().prefetch_related('cartitems__product')
        serializer = order_serializer(orders, many=True)
        return Response(serializer.data)
    # Handle the order passing logic for customers and guests
    def post(self, request):
        if request.user.is_authenticated:
            return self.passing_order_for_customer(request)
        else:
            return self.passing_order_for_guest(request)
    # Passing order Logic for Guests
    def passing_order_for_guest(self, request):
        guest_id = request.session.session_key
        if not guest_id:
            return Response({"message": "Guest session not found"}, status=status.HTTP_400_BAD_REQUEST)
        cart_items = CartItems.objects.filter(guest_id=guest_id).select_related('product')
        if not cart_items.exists():
            return Response({"message": "No cart items found for guest"}, status=status.HTTP_400_BAD_REQUEST)
        order = Order.objects.create()
        order.cartitems.set(cart_items)  
        order.save()
        return Response({"message": "Order passed"}, status=status.HTTP_200_OK)
    # Passing order Logic for Customers
    def passing_order_for_customer(self,request):
        customer = Customer.objects.get(user=request.user)
        cart_items = CartItems.objects.filter(customer=customer).select_related('product')
        if not cart_items.exists():
            return Response({"message": "No cart items found for customer"}, status=status.HTTP_400_BAD_REQUEST)
        order = Order.objects.create()
        order.cartitems.set(cart_items)
        order.save()
        return Response({"message": "Order passed"}, status=status.HTTP_200_OK)