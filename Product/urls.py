from django.urls import path
from . import views

urlpatterns = [
    path('all_products/' , views.products_api_view.as_view()),
    path('add_product/' , views.AddProductView.as_view()),
    path('product/<int:pk>/' , views.single_product_api_view.as_view()),
]