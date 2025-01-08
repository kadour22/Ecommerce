from django.urls import path
from . import views

urlpatterns = [
    path('customers-view/' , views.create_customer_view.as_view(),name='customer'),
    path('manage-customer/' , views.updated_customer_data.as_view(),name='manage-customer'),
]