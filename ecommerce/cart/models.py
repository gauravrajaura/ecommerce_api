from itertools import product
from statistics import mode
from tkinter import CASCADE
from unicodedata import category
from django.db import models

from django.contrib.auth.models import User

from django.utils import timezone



class Catergory(models.Model):
    #category_id=models.IntegerField(primary_key=True,default='null')
    name= models.CharField(max_length=100)

    
    def __str__(self):
        return self.name

class Product(models.Model):

    product_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=15)
    category= models.ForeignKey(Catergory, on_delete=models.CASCADE,related_name="category")
    price = models.FloatField()
    brand = models.CharField(max_length=1000)
    date_added = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.product_name

class Cart(models.Model):
    
    cart_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete = models.CASCADE,related_name="user")
    created_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return (f"{self.user}'s cart")  

class ProductInCart(models.Model):
    
    class Meta:
        unique_together = (('cart', 'product'),)
    
    product_in_cart_id = models.AutoField(primary_key=True)
    cart = models.ForeignKey(Cart, on_delete = models.CASCADE,related_name="cart")
    product = models.ForeignKey(Product, on_delete = models.CASCADE,related_name="product")
    quantity = models.PositiveIntegerField()


class Order(models.Model):
    
    status_choices = (
        (1, 'Not Packed'),
        (2, 'Ready For Shipment'),
        (3, 'Shipped'),
        (4, 'Delivered')
    )
    payment_status_choices = (
        (1, 'SUCCESS'),
        (2, 'FAILURE' ),
        (3, 'PENDING'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField(choices = status_choices, default=1)
   # product= models.ManyToManyField(Product,on_delete=models.CASCADE)
    total_amount = models.FloatField()
    payment_status = models.IntegerField(choices = payment_status_choices, default=3)
    order_id = models.CharField(unique=True, max_length=100, null=True, blank=True, default=None) 
    datetime_of_payment = models.DateTimeField(default=timezone.now)
