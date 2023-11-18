from rest_framework import serializers
from api.models.product_models import Product
from .product_reviews_serializers import ProductReviewSerializer


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields="__all__"

    def __init__(self, *args, **kwargs):
        super(ProductListSerializer, self).__init__(*args,**kwargs)
        self.Meta.depth=1


class ProductDetailSerializer(serializers.ModelSerializer):
    product_reviews= ProductReviewSerializer
    class Meta:
        model = Product
        fields=["id","title","description","price","vendor","product_category"]

