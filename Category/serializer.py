from rest_framework import serializers
from .models import Category

class category_serializer(serializers.ModelSerializer) :
    class Meta :
        model = Category
        fields = "__all__"