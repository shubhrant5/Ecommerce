from django.contrib import admin
from .models import User, Order, Category, Products, Cart, Order_List
# Register your models here.
admin.site.register(User)
admin.site.register(Products)
admin.site.register(Order)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(Order_List)
