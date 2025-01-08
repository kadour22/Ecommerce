from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin
from .models import CartItems
from .serializer import cartitems_serializer
from Customer.models import Customer

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
