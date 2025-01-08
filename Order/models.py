from django.db import models
from CartItems.models import CartItems
from uuid import uuid4


class Order(models.Model):
    cartitems = models.ManyToManyField(CartItems)
    order_id  = models.CharField(max_length=255 , default=uuid4)
    created_at = models.DateTimeField(auto_now_add=True)