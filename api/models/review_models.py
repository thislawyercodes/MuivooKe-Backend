
from django.db import models
from django.contrib.auth.models import User
from api.base_model import BaseModel
from .product_models import Product

class ProductReviews(BaseModel):
    customer=models.ForeignKey(User,on_delete=models.CASCADE,related_name="customer_reviews+")
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="product_reviews+")
    description=models.TextField(blank=True,null=True)
    review_time=models.DateTimeField(auto_now_add=True)
    rating=models.IntegerField(null=True)
  
    def __str__(self):
        return f'  Rating for {self.product.title} {self.rating}- {self.description} by {self.customer.username} at {self.review_time} '

