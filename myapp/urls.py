from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import UserViewSet, ProfileViewSet, CategoryViewSet, ProductViewSet, OrderViewSet, notifications_test, index

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('index/', index, name='index.html'),
    path('notifications-test/', notifications_test, name='notifications_test'),

]
