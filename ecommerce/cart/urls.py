from django.urls import path,include
from rest_framework.routers import DefaultRouter

from .views import (
    UserViewSet,
    CategoryViewSet,
    ProductViewSet,
    CartViewSet,
    ProductInCartViewSet,
    OrderViewSet,
    OrderListApiView,
    OrderDetailApiView
)


router= DefaultRouter()
router.register('Userviewsetapi',UserViewSet,basename='user')
router.register('Categoryviewsetapi',CategoryViewSet,basename='catergory')
router.register('Productviewsetapi',ProductViewSet,basename='product')
router.register('Cartviewsetapi',CartViewSet,basename='cart')
router.register('ProductInCartviewsetapi',ProductInCartViewSet,basename='product_in_cart')
router.register('Orderviewset',OrderViewSet,basename='order')


urlpatterns=router.urls


'''urlpatterns = [
   # path('/order', OrderListApiView.as_view()),
   #path('order/<int:order_id>/',OrderDetailApiView.as_view()),

]'''
