from rest_framework import serializers
from api.models.review_models import ProductReviews


class ProductReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReviews
        fields=["id","customer","product","description","review_time","rating"]

    def __init__(self, *args, **kwargs):
        super(ProductReviewSerializer, self).__init__(*args,**kwargs)
        self.Meta.depth=1