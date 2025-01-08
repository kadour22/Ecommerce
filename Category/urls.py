from django.urls import path
from . import views

urlpatterns = [
    path('create-category/' , views.category_api_view.as_view()),
    path('manage-category/<int:pk>/' , views.manage_category_view.as_view()),
]