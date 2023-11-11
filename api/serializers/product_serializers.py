from rest_framework import serializers
from api.models.product_models import Product


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields="__all__"

    def __init__(self, *args, **kwargs):
        super(ProductListSerializer, self).__init__(*args,**kwargs)
        self.Meta.depth=1