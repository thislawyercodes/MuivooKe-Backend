
from django.db import models
from django.contrib.auth.models import User
from api.base_model import BaseModel
from api.models.vendor_models import Vendor



class ProductCategory(BaseModel):
    title=models.CharField(max_length=250)
    description=models.TextField(max_length=200)

    def __str__(self):
        return self.title


class Product(BaseModel):
    title=models.CharField(max_length=250)
    description=models.TextField(max_length=200)
    price=models.FloatField(default=0.0)
    product_category=models.ForeignKey(ProductCategory,on_delete=models.SET_NULL,null=True)
    vendor=models.ForeignKey(Vendor,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.title


    


