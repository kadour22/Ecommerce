from django.urls import path
from . import views


urlpatterns = [
    path("passding_order/" , views.passing_order_api_view.as_view(),name='passing_order'),
]