from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin
from .models import CartItems
from .serializer import cartitems_serializer
from Customer.models import Customer
from .utils import add_or_update_cartitems_for_customers , add_or_update_cartitems_for_guest_user
class AddToCartView(GenericAPIView,CreateModelMixin):
    serializer_class = cartitems_serializer
    def post(self,request,*args,**kwargs) :
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid() :
            product = serializer.validated_data['product']
            quantity = serializer.validated_data['quantity']
            if request.user.is_authenticated:
                cart_item = self.add_or_update_cartitems_for_customers(product,quantity)
            else:
                cart_item = self.add_or_update_cartitems_for_guest_user(product,quantity)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)   
   
class delete_product_cart(GenericAPIView , CreateModelMixin):
    def post(self , request , id):
        cart_items = get_object_or_404(CartItems , id=id)
        cart_items.save()
        return Response('removed')
    
class IncrementProductQuantity(APIView):
    def get_object(self , cart_items_id):
        try :
            return CartItems.objects.get(id=cart_items_id)
        except CartItems.DoesNotExist :
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def patch(self , request , cart_items_id) :
        cartitems = self.get_object(cart_items_id)
        cartitems.quantity += 1
        cartitems.save()
        return Response({'message :' : 'product quantity updated '})
    
class DecrementProductQuantity(APIView) :
    def get_object(self , cart_items_id):
        try :
            return CartItems.objects.get(id=cart_items_id)
        except CartItems.DoesNotExist :
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def patch(self , request , cart_items_id) :
        cartitems = self.get_object(cart_items_id)
        cartitems.quantity -= 1
        cartitems.save()
        return Response({'message :' : 'product quantity updated '})

class my_cartitems_api_view(APIView):
    serializer_class = cartitems_serializer
    def get(self , request , *args , **kwargs):
        if request.user.is_authenticated:
           customer = get_object_or_404(Customer , user=request.user)
           cart_items = CartItems.objects.filter(customer=customer)
           serializer = cartitems_serializer(cart_items , many=True)
           return Response(serializer.data , status=status.HTTP_200_OK)
        else:
            cart_items = CartItems.objects.filter(guest_id=request.session.session_key)
            serializer = cartitems_serializer(cart_items , many=True)
            return Response(serializer.data , status=status.HTTP_200_OK)
