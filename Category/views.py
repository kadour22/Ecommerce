from rest_framework import generics , status , permissions
from .models import Category
from .serializer import category_serializer


class category_api_view(generics.ListCreateAPIView) :
    queryset = Category.objects.all()
    serializer_class = category_serializer
    permission_classes = [permissions.IsAdminUser]

class manage_category_view(generics.RetrieveUpdateDestroyAPIView) :
    serializer_class = category_serializer
    queryset = Category.objects.all()
    lookup_field = 'pk'
    permission_classes = [permissions.IsAdminUser]