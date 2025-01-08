from django.urls import path
from . import views

urlpatterns = [
    path('add-to-cart/', views.AddToCartView.as_view() , name='add') , 
    path('increment/<int:cart_items_id>/', views.IncrementProductQuantity.as_view() , name='encrement') , 
    path('derement/<int:cart_items_id>/', views.DecrementProductQuantity.as_view() , name='derement') , 
    path('remove/<int:id>/', views.delete_product_cart.as_view() , name='remove') , 
    path('my-cart/', views.my_cartitems_api_view.as_view() , name='mycart') ,
]
