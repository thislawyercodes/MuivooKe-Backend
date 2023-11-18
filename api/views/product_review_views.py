from django.shortcuts import render
from rest_framework import generics,permissions
from api.models.review_models import ProductReviews
from api.serializers.product_reviews_serializers import ProductReviewSerializer

class ProductReviewListApiView(generics.ListCreateAPIView):
    queryset = ProductReviews.objects.all()
    serializer_class=ProductReviewSerializer

class ProductReviewDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[permissions.IsAuthenticated]
    queryset = ProductReviews.objects.all()
    serializer_class=  ProductReviewSerializer
