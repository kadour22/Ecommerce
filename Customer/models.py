from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name='customer')
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    adress = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
