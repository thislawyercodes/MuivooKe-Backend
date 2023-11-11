from django.db import models
import uuid


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now=True, editable=False)
    modified_at = models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(unique=True,default=uuid.uuid4,primary_key=True)

    class Meta:
        abstract = True
