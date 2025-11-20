
from .models import CartItems
from Customer.models import Customer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status

def get_the_current_session(self):
        sessionID = self.request.session.session_key
        if not sessionID:
            sessionID = self.request.session.create()
        return sessionID      
def add_or_update_cartitems_for_guest_user(self,product,quantity):
        cart_items = CartItems.objects.filter(product=product , guest_id=self.get_the_current_session())
        if cart_items.exists():
            cart_item = cart_items.first()
            cart_item.quantity += quantity
            cart_item.save()
            return Response({'message :' : 'product quantity updated '}, status=status.HTTP_200_OK)
        else:
            cart_item = CartItems.objects.create(product=product , quantity=quantity , guest_id=self.get_the_current_session())
            cart_item.save()
            return Response({'message :' : 'product added to cart '}, status=status.HTTP_201_CREATED)
        return cart_item
def add_or_update_cartitems_for_customers(self, product, quantity):
        customer = get_object_or_404(Customer, user=self.request.user)
        cart_items = CartItems.objects.filter(product=product, customer=customer)
        if cart_items.exists():
            cart_item = cart_items.first()
            cart_item.quantity += quantity
            cart_item.save()
            return Response({'message': 'Product quantity updated'}, status=status.HTTP_200_OK)
        else:
            cart_item = CartItems.objects.create(product=product, quantity=quantity, customer=customer)
            cart_item.save()
            return Response({'message': 'Product added to cart'}, status=status.HTTP_201_CREATED)
