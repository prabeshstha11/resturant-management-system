from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Food(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    
class Table(models.Model):
    number = models.CharField(max_length=2)
    capacity = models.IntegerField()
    is_available = models.BooleanField(default=True)
    
    def __str__(self):
        return self.number
    
class Order(models.Model):
    STATUS_CHOICE = [
        ('pending', 'PENDING'),
        ('completed', "COMPLETED"),
        ('delivered', 'DELIVERED')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICE,
        default='pending'
    )
    
class OrderedFood(models.Model):
    food = models.ForeignKey(Food, on_delete=models.PROTECT)
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    
class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    is_paid = models.BooleanField(default=False)

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.PROTECT)