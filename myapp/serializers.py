from rest_framework import serializers
from .models import User, Profile, Product, Category, Order



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class ProfileSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Profile
        fields = ['id', 'user', 'bio']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'category']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:    
        model = Order
        fields = ['id', 'user', 'products', 'created_at']




