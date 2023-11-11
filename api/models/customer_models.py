
from django.db import models
from django.contrib.auth.models import User
from api.base_model import BaseModel
from .product_models import Product

class Customer(BaseModel):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    phone_number=models.CharField(max_length=25)
    address_number=models.CharField(max_length=200)

    def __str__(self):
        return self.user.username

class Order(BaseModel):
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_time=models.DateTimeField(auto_now_add=True)
   

class OrderItem(BaseModel):
    order=models.ForeignKey(Order, on_delete=models.CASCADE,related_name="order_item")
    product=models.ForeignKey(Product, on_delete=models.CASCADE)


