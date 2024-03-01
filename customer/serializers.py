from rest_framework import serializers
from .models import Cart,Order_List, Order,User, Products,Category


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields ='__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields ='__all__'
        depth = 1
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields ='__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields ='__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields ='__all__'
        depth = 1
