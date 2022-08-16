from django.contrib import admin
from .models import *

admin.site.register(Product)
admin.site.register(Catergory)
admin.site.register(Cart)
admin.site.register(ProductInCart)
admin.site.register(Order)

