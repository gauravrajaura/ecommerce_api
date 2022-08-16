from asyncio import tasks
from dataclasses import fields
from imp import source_from_cache
from os import read
from pyexpat import model
from re import T
from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from .models import *
#from .models import status_choices , payment_status_choices

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"

class CatergorySerializer(serializers.Serializer):
    #category_id=serializers.IntegerField()   
    name= serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Catergory.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

'''
class ProductSerializer(serializers.ModelSerializer):
    catergory_id = CatergorySerializer(read_only=True,many=True)
    class Meta:
        model=Product
        fields=('product_id','product_name','price','brand','date_added','catergory_id')
    
    
    
    category = CatergorySerializer()
    category = serializers.RelatedField(source="catergory",read_only=True)
    #category_name = serializers.CharField(source='category.name')
    product_id = serializers.IntegerField()
    product_name = serializers.CharField(max_length=15)
    #category= serializers.ForeignKey(Catergory, on_delete=models.CASCADE)
    price = serializers.FloatField()
    brand = serializers.CharField(max_length=1000)
    date_added = serializers.DateTimeField(default=timezone.now)
    
    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.product_id = validated_data.get('product_id', instance.product_id)
        instance.product_name = validated_data.get('product_name', instance.product_name)
        #instance.category = validated_data.get('category', instance.category)
        instance.price = validated_data.get('price', instance.price)
        instance.brand = validated_data.get('brand', instance.brand)
        #instance.date_added = validated_data.get('date_added', instance.date_added)
        instance.save()
        return instance'''

class ProductSerializer(serializers.ModelSerializer):
   # category = CatergorySerializer()
    category = serializers.StringRelatedField(read_only=True)

    class Meta:
        model=Product
        fields = "__all__"


class CartSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    class Meta:
        model=Cart
        fields = "__all__"

    def create(self, validated_data):
        user_id = UserSerializer.create(UserSerializer(), validated_data)
        user, created = User.objects.create(user=user_id)
        return user

class ProductInCartSeializer(serializers.ModelSerializer):
    cart = serializers.StringRelatedField(read_only=True)
    product = serializers.StringRelatedField(read_only=True)

    class Meta:
       model=ProductInCart
       fields="__all__"


class OrderSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=Order
        fields="__all__"


'''
class ProductInCartSerializer(serializers.Serializer):
    
    product_in_cart_id = serializers.AutoField(primary_key=True)
    cart = serializers.ForeignKey(Cart, on_delete = models.CASCADE)
    product = serializers.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = serializers.PositiveIntegerField()

    
    def create(self, validated_data):
        return ProductInCart.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.product_in_cart_id = validated_data.get('product_in_cart_id', instance.product_in_cart_id)
        instance.cart = validated_data.get('cart', instance.cart)
        instance.product = validated_data.get('product', instance.product)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.save()
        return instance

class OrderSerializer(serializers.Serializer):
    
    product_in_cart_id = serializers.AutoField(primary_key=True)
    cart = serializers.ForeignKey(Cart, on_delete = models.CASCADE)
    product = serializers.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = serializers.PositiveIntegerField()

    user = serializers.ForeignKey(User, on_delete=models.CASCADE)
    status = serializers.IntegerField(choices = status_choices, default=1)
    total_amount = serializers.FloatField()
    payment_status = serializers.IntegerField(choices = payment_status_choices, default=3)
    order_id = serializers.CharField(unique=True, max_length=100, null=True, blank=True, default=None) 
    datetime_of_payment = serializers.DateTimeField(default=timezone.now)
    
    def create(self, validated_data):
        return Order.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.status = validated_data.get('status', instance.status)
        instance.total_amount = validated_data.get('total_amount', instance.total_amount)
        instance.payment_status = validated_data.get('payment_status', instance.payment_status)
        instance.order_id = validated_data.get('order_id', instance.order_id)
        instance.datetime_of_payment = validated_data.get('datetime_of_payment', instance.datetime_of_payment)
        instance.save()
        return instance
'''