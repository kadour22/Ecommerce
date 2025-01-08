from django.db import models
from Customer.models import Customer
from Product.models import Product

class CartItems(models.Model) :
    guest_id = models.CharField(max_length=255 , null=True)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT , related_name='cartitems',null=True)
    product  = models.ForeignKey(Product, on_delete=models.PROTECT , related_name='cartitems')
    quantity = models.PositiveIntegerField()

    
    class Meta :
        unique_together = ('product','guest_id')

    # def __str__(self):
    #     return f"CartItem: {self.product.product_name} (Quantity: {self.quantity})"    