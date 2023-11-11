
from django.db import models
from django.contrib.auth.models import User
from api.base_model import BaseModel

class Vendor(BaseModel):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    phone_number=models.CharField(max_length=25)
    address_number=models.CharField(max_length=200)

    def __str__(self):
        return self.user.username

