from django.shortcuts import render
from rest_framework import generics,permissions
from api.models.product_models import Product
from api.serializers.product_serializers import ProductListSerializer,ProductDetailSerializer

class ProductListApiView(generics.ListCreateAPIView):
    permission_classes=[permissions.IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class=ProductListSerializer

class ProductDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[permissions.IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class=  ProductDetailSerializer
