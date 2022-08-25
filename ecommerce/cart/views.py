from typing import Generic
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import status
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
from ecommerce import settings
from rest_framework import pagination

class CustomPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 50
    page_query_param = 'p'

    def get_paginated_response(self, data):
        response = Response(data)
        response['count'] = self.page.paginator.count
        response['next'] = self.get_next_link()
        response['previous'] = self.get_previous_link()
        return response
'''class PaginationClass(PageNumberPagination):
    page_size = 5
    max_page_size = 10
'''
#------------------------------------------------USER--------------------------------------------------------#

#   USER VIEWSET
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

#   USER GENERIC-API-VIEW
class UserGenericView(generics.GenericAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    pagination_class= CustomPagination
    
    '''def get_queryset(self, *args, **kwargs):
        return User.objects.all()'''

    def get(self, request, *args, **kwargs):
        order = User.objects.all()
        serializer = UserSerializer(order, many=True)
        #queryset = self.get_queryset()
        #paginated_queryset = self.pagination_class.paginate_queryset(queryset,request)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request, *args, **kwargs):
        data = {
        
            'password': request.data.get('password'),
            'is_superuser': request.data.get('is_superuser'),
            'username': request.data.get('username'),
            'first_name': request.data.get('first_name'),
            'last_name': request.data.get('last_name'),
            'email': request.data.get('email'),
            'is_staff': request.data.get('is_staff'),
            'is_active': request.data.get('is_active'),
            'is_staff': request.data.get('is_staff'),
            'date_joined': request.data.get('date_joined'),
            }
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class UserdetailGenericView(generics.GenericAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    pagination_class=PageNumberPagination

    def get_object_with_id(self, user_id):
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None
    def get(self, request, user_id, *args, **kwargs):
        user_instance = self.get_object_with_id(user_id)
        if not user_instance:
            return Response(
                {"result": "Object with user id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = UserSerializer(user_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def delete(self, request, user_id, *args, **kwargs):
        user_instance = self.get_object_with_id(user_id)
        if not user_instance:
            return Response(
                {"res": "Object with user id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        user_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )

#------------------------------------------------CATEGORY--------------------------------------------------------#

#    CATEGORY VIEWSET
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

#   CATEGORY GENERIC-API-VIEW
class CategoryGenericView(generics.GenericAPIView):
    queryset=Catergory.objects.all()
    serializer_class=CatergorySerializer
    #pagination_class=PageNumberPagination

    def get(self, request, *args, **kwargs):
        catergory = Catergory.objects.all()
        serializer = CatergorySerializer(catergory, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request, *args, **kwargs):
        data = {
            'name': request.data.get('name'),
            }
        serializer = CatergorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class CategorydetailGenericView(generics.GenericAPIView):
    queryset=Catergory.objects.all()
    serializer_class=CatergorySerializer
    pagination_class=PageNumberPagination

    def get_object_with_id(self, catergory_id):
        try:
            return Catergory.objects.get(id=catergory_id)
        except Catergory.DoesNotExist:
            return None
    def get(self, request, catergory_id, *args, **kwargs):
        catergory_instance = self.get_object_with_id(catergory_id)
        #print('nagasdfasd')
        if not catergory_instance:
            return Response(
                {"result": "Object with Category id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = CatergorySerializer(catergory_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def delete(self, request, catergory_id, *args, **kwargs):
        catergory_instance = self.get_object_with_id(catergory_id)
        if not catergory_instance:
            return Response(
                {"res": "Object with category id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        catergory_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )
    def put(self, request, catergory_id, *args, **kwargs):
        catergory_instance = self.get_object_with_id(catergory_id)
        if not catergory_instance:
            return Response(
                {"res": "Object with Category id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'name': request.data.get('name'), 
            }
        serializer = CatergorySerializer(instance = catergory_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#-------------------------------------------------PRODUCT--------------------------------------------------------#

#    PRODUCT VIEWSET
class ProductViewSet(viewsets.ViewSet):
   # pagination_class=PaginationClass
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
        import ipdb; ipdb.set_trace()
        print("line_76")
        serializer = ProductSerializer(data=request.data)
        print("line_78")
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
#    PRODUCT GENERIC-API-VIEW
class ProductGenericView(generics.GenericAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    def get(self, request, *args, **kwargs):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request, *args, **kwargs):
        data = {
            'product_id': request.data.get('product_id'), 
            'category': request.data.get('category'), 
            'product_name':request.data.get('product_name'),
            'price':request.data.get('price'),
            'brand':request.data.get('brand'),
            'date_added':request.data.get('date_added')
            }
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ProductdetailGenericView(generics.GenericAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    pagination_class=PageNumberPagination

    def get_object_with_id(self, product_id):
        try:
            return Product.objects.get(product_id=product_id)
        except Product.DoesNotExist:
            return None
    def get(self, request, product_id, *args, **kwargs):
        product_instance = self.get_object_with_id(product_id)
        #print('nagasdfasd')
        if not product_instance:
            return Response(
                {"result": "Object with Category id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = ProductSerializer(product_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def delete(self, request, product_id, *args, **kwargs):
        product_instance = self.get_object_with_id(product_id)
        if not product_instance:
            return Response(
                {"res": "Object with category id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        product_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )
    def put(self, request, product_id, *args, **kwargs):
        product_instance = self.get_object_with_id(product_id)
        if not product_instance:
            return Response(
                {"res": "Object with Category id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'product_id': request.data.get('product_id'), 
            'category': request.data.get('category'), 
            'product_name': request.data.get('product_name'), 
            'price': request.data.get('price'), 
            'brand': request.data.get('brand'), 
            'date_added': request.data.get('date_added'),
            }
        serializer = ProductSerializer(instance = product_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#--------------------------------------------------CART--------------------------------------------------------#

#    CART VIEWSET
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

#----------------------------------------------PRODUCT_IN_CART--------------------------------------------------------#

#    PRODUCT_IN_CART VIEWSET
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
#    PRODUCT_IN_CART GENERIC-API-VIEW
class ProductInCartGenericView(generics.GenericAPIView):
    queryset=ProductInCart.objects.all()
    serializer_class=ProductInCartSeializer
    def get(self, request, *args, **kwargs):
        product_in_cart = ProductInCart.objects.all()
        serializer = ProductInCartSeializer(product_in_cart, many=True)
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
        serializer = ProductInCartSeializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ProductInCartDetailGenericView(generics.GenericAPIView):
    queryset=ProductInCart.objects.all()
    serializer_class=OrderSerializer
    def get_object_with_id(self, order_id):
        try:
            return ProductInCart.objects.get(id=order_id)
        except ProductInCart.DoesNotExist:
            return None
    def delete(self, request, product_in_cart_id, *args, **kwargs):
        order_instance = self.get_object_with_id(product_in_cart_id)
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

#------------------------------------------------ORDER--------------------------------------------------------#

#   ORDER VIEWSET
class OrderViewSet(viewsets.ViewSet):
    def list(self, request):
        order = Order.objects.all()
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def retrieve(self,request,pk=None):
        id=pk
        if id is not None:
            order = Order.objects.get(id=id)
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
#   ORDER APIVIEW
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
#   ORDER GENERIC-API-VIEW
class OrderGenericView(generics.GenericAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer
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
    queryset=Order.objects.all()
    serializer_class=OrderSerializer
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