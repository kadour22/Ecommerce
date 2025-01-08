from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status , permissions , generics
from .models import Customer
from .serializer import customer_serializer
from .permission import customer_permissions

class create_customer_view(APIView) :
    
    def post(self , request , *args , **kwargs) :
        serializer = customer_serializer(data=request.data)
        if serializer.is_vaslid() :
            customer = serializer.save()
            return Response({'message': f'{customer} your account created..💕'} , status=status.HTTP_201_CREATED)
        return  Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
    def get(self , request, *args , **kwargs) :
        user = request.user.customer
        customer = Customer.objects.get(user=user)
        serializer = customer_serializer(customer)
        return Response(serializer.data , status=status.HTTP_200_OK)
    
class updated_customer_data(generics.RetrieveUpdateAPIView) :
    serializer_class = customer_serializer
    queryset = Customer.objects.all()
    permission_classes = [customer_permissions]
    lookup_field = 'pk' 