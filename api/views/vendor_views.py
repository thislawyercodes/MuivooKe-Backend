from django.shortcuts import render
from rest_framework import generics,permissions
from api.models.vendor_models import Vendor
from api.serializers.vendor_serializers import  VendorListSerializer

class VendorListApiView(generics.ListCreateAPIView):
    permission_classes=[permissions.IsAuthenticated]
    queryset = Vendor.objects.all()
    serializer_class=VendorListSerializer

class VendorDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[permissions.IsAuthenticated]
    queryset = Vendor.objects.all()
    serializer_class= VendorListSerializer
