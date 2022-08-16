from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import status
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

class PaginationClass(PageNumberPagination):
    page_size = 5
    max_page_size = 10

class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def retrieve(self,request,pk=None):
        id=pk
        if id is not None:
            user = User.objects.get(id=id)
            serializer = UserSerializer(user)
            return Response(serializer.data)

class CategoryViewSet(viewsets.ViewSet):
    def list(self, request):
        category = Catergory.objects.all()
        serializer = CatergorySerializer(category, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def retrieve(self,request,pk=None):
        id=pk
        if id is not None:
            category = Catergory.objects.get(category_id=id)
            serializer = CatergorySerializer(category)
            return Response(serializer.data)
    def create(self, request):
        serializer = CatergorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def update(self, request, pk=None):
        id=pk
        category = Catergory.objects.get(category_id=id)
        serializer = CatergorySerializer(category,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def destroy(self, request, pk=None):
        id=pk
        category = Catergory.objects.get(category_id=id)
        category.delete()
        return Response({'msg':'Data Deleted'},status=status.HTTP_204_NO_CONTENT)

class ProductViewSet(viewsets.ViewSet):
    pagination_class=PaginationClass
    def list(self, request):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def retrieve(self,request,pk=None):
        id=pk
        if id is not None:
            product = Product.objects.get(product_id=id)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def update(self, request, pk=None):
        id=pk
        product = Product.objects.get(product_id=id)
        serializer = CatergorySerializer(product,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def partial_update(self, request, pk=None):
        id=pk
        product = Product.objects.get(product_id=id)
        serializer = ProductSerializer(product,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated Partialy'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def destroy(self, request, pk=None):
        id=pk
        product = Product.objects.get(product_id=id)
        product.delete()
        return Response({'msg':'Data Deleted'},status=status.HTTP_204_NO_CONTENT)

class CartViewSet(viewsets.ViewSet):
    def list(self, request):
        cart = Cart.objects.all()
        serializer = CartSerializer(cart, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def retrieve(self,request,pk=None):
        id=pk
        if id is not None:
            product = Cart.objects.get(cart_id=id)
            serializer = CartSerializer(product)
            return Response(serializer.data)
    def create(self, request):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def update(self, request, pk=None):
        id=pk
        cart = Cart.objects.get(cart_id=id)
        serializer = CartSerializer(cart,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def partial_update(self, request, pk=None):
        id=pk
        cart = Cart.objects.get(cart_id=id)
        serializer = CartSerializer(cart,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated Partialy'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def destroy(self, request, pk=None):
        id=pk
        cart = Cart.objects.get(product_id=id)
        cart.delete()
        return Response({'msg':'Data Deleted'},status=status.HTTP_204_NO_CONTENT)

class ProductInCartViewSet(viewsets.ViewSet):
    def list(self, request):
        productInCart = ProductInCart.objects.all()
        serializer = ProductInCartSeializer(productInCart, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def create(self, request):
        serializer = ProductInCartSeializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def destroy(self, request, pk=None):
        id=pk
        productInCart = ProductInCart.objects.get(product_id=id)
        productInCart.delete()
        return Response({'msg':'Data Deleted'},status=status.HTTP_204_NO_CONTENT)

class OrderViewSet(viewsets.ViewSet):
    def list(self, request):
        order = Order.objects.all()
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def retrieve(self,request,pk=None):
        id=pk
        if id is not None:
            order = Order.objects.get(cart_id=id)
            serializer = OrderSerializer(order)
            return Response(serializer.data)
    def create(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def destroy(self, request, pk=None):
        id=pk
        order = Order.objects.get(product_id=id)
        order.delete()
        return Response({'msg':'Data Deleted'},status=status.HTTP_204_NO_CONTENT)

class OrderListApiView(APIView):
    def get(self, request, *args, **kwargs):
        order = Order.objects.all()
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'user': request.data.get('user'), 
            'status': request.data.get('status'), 
            'total_amount':request.data.get('total_amount'),
            'payment_status':request.data.get('payment_status'),
            'order_id':request.data.get('order_id'),
            'datetime_of_payment':request.data.get('datetime_of_payment')
            }
        serializer = OrderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderDetailApiView(APIView):

    def get_object_with_id(self, order_id):
        try:
            return Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            return None

    def get(self, request, order_id, *args, **kwargs):
        order_instance = self.get_object_with_id(order_id)
        if not order_instance:
            return Response(
                {"result": "Object with order id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = OrderSerializer(order_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, order_id, *args, **kwargs):
        order_instance = self.get_object_with_id(order_id)
        if not order_instance:
            return Response(
                {"res": "Object with todo id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'user': request.data.get('user'), 
            'status': request.data.get('status'), 
            'total_amount':request.data.get('total_amount'),
            'payment_status':request.data.get('payment_status'),
            'order_id':request.data.get('order_id'),
            'datetime_of_payment':request.data.get('datetime_of_payment')
            }
        serializer = OrderSerializer(instance = order_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, order_id, *args, **kwargs):
        order_instance = self.get_object_with_id(order_id)
        if not order_instance:
            return Response(
                {"res": "Object with todo id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        order_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )
