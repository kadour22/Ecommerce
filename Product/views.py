from rest_framework import generics , permissions , status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import Product
from .serializer import product_serializer

from django.core.cache import cache
class products_api_view(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        cache_key = 'products'
        cache_products = cache.get(cache_key)
        if cache_products:
            return Response(cache_products)
        else:
            products = Product.objects.all()
            paginator = PageNumberPagination()
            paginator.page_size = 2  # Number of items per page
            result_page = paginator.paginate_queryset(products, request)
            serializer = product_serializer(result_page, many=True)
            paginated_response = paginator.get_paginated_response(serializer.data)
            cache.set(cache_key, paginated_response.data, timeout=60*60)
            return paginated_response

class single_product_api_view(generics.RetrieveAPIView) :
    queryset = Product.objects.all()
    serializer_class = product_serializer
    permission_classes = [permissions.AllowAny]    
    lookup_field = 'pk'


class AddProductView(generics.CreateAPIView) :
    queryset = Product.objects.all()
    serializer_class = product_serializer
    permission_classes = [permissions.IsAdminUser]
