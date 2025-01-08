from django.db import models
from Category.models import Category

class Product(models.Model):
    product_name  = models.CharField(max_length=255)
    product_price = models.DecimalField(max_digits=8,decimal_places=3)
    product_image = models.ImageField(upload_to='product')
    descriptions = models.TextField()
    in_stock = models.PositiveIntegerField()

    category = models.ForeignKey(Category , on_delete=models.PROTECT , related_name='product')
