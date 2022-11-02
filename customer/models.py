from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
import datetime
# Create your models here.
class User(AbstractUser):
    username=None
    email=models.EmailField(unique=True)
    Address =models.CharField(max_length=100)
    Phone_number=models.CharField(max_length=15)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Category(models.Model):
    name = models.CharField(max_length=50)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=60)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=250, default='', blank=True, null=True)
    image = models.ImageField(upload_to='images')

    @staticmethod
    def get_products_by_id(ids):
        return Products.objects.filter(id__in=ids)

    @staticmethod
    def get_all_products():
        return Products.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Products.objects.filter(category=category_id)
        else:
            return Products.get_all_products()

class Order(models.Model):
    customer = models.ForeignKey(User,
                                 on_delete=models.CASCADE)
    price = models.IntegerField()
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')

class Order_List(models.Model):
    order = models.ForeignKey(Order,
                                 on_delete=models.CASCADE)
    product = models.ForeignKey(Products,
                                on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    @staticmethod
    def get_order_list_by_id(order_id):
        return Order_List.objects.filter(order=order_id)

class Cart(models.Model):
    product = models.ForeignKey(Products,
                                on_delete=models.CASCADE)
    customer = models.ForeignKey(User,
                                 on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    status = models.BooleanField(default=False)

    @staticmethod
    def get_products_from_cart(product_id):
        return Cart.objects.filter(product=product_id)

    @staticmethod
    def get_cart_by_customer(customer_id):
        return Cart.objects.filter(customer=customer_id)
