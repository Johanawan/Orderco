from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(default="profile.png",null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.name)

class Product(models.Model):
    EAT_OPTION = (
        ("Collection", "Collection"),
        ("Delivery", "Delivery"),
    )
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(max_length=200)
    eating_option = models.CharField(max_length=200, null=True, choices=EAT_OPTION)
    description = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tag = models.ManyToManyField(Tag)


    def __str__(self):
        return str(self.name)

class Order(models.Model):
    ORDER_STATUS = (
        ("Pending", "Pending"),
        ("Out For Delivery", "Out For Delivery"),
        ("Delivered", "Delivered"),
    )

    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL) 
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    order_status = models.CharField(max_length=200, null=True, choices=ORDER_STATUS)
    note = models.CharField(max_length=1000, null=True, choices=ORDER_STATUS)

    def __str__(self):
        return str(self.product.name)

