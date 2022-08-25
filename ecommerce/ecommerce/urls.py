"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from cart import urls as category_urls
from cart.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(category_urls)),
    path('user/',UserGenericView.as_view()),
    path('user/<int:user_id>',UserdetailGenericView.as_view()),
    path('order/', OrderListApiView.as_view()),
    path('order/<int:order_id>', OrderDetailApiView.as_view()),
    path('category/', CategoryGenericView.as_view()),
    path('category/<int:catergory_id>', OrderDetailApiView.as_view()),
    path('product/',ProductGenericView.as_view()),
    path('product/<int:product_id>', ProductdetailGenericView.as_view()),



]
