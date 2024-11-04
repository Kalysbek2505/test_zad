from django.db import models



class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)


    def __str__(self):
        return self.username
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()


    def __str__(self):
        return f'Профиль {self.user.username}'



class Category(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self) -> str:
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    

    def __str__(self) -> str:
        return self.name
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    products = models.ManyToManyField(Product, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return f'Заказ {self.id} {self.user.username}'
    