from django.contrib import admin

from apps.orders.models import Order, ProductPurchase

admin.site.register(Order)

admin.site.register(ProductPurchase)
