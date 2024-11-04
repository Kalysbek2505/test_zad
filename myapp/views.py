from asgiref.sync import async_to_sync
from django.shortcuts import render
from channels.layers import get_channel_layer
from rest_framework import viewsets
from .models import User, Profile, Product, Category, Order
from .serializers import UserSerializer, ProfileSerializer, ProductSerializer, CategorySerializer, OrderSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        # Отправка уведомления через канал при создании нового пользователя
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "notifications",
            {
                "type": "send_notification",
                "message": f"Новый пользователь создан: {user.username}"
            }
        )


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer



def index(request):
    return render(request, 'index.html')

def notifications_test(request):
    return render(request, 'notifications_test.html')

