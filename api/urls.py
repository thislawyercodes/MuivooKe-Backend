from django.urls import path 
from .views.vendor_views import VendorListApiView,VendorDetailApiView
from .views.product_views import ProductListApiView,ProductDetailApiView


app_name = 'api'

urlpatterns =[
    path('vendors',VendorListApiView.as_view(),name='api_vendor_list'),
    path('vendors/<str:pk>/',VendorDetailApiView.as_view(),name='api_vendor_detail'),
    path('products',ProductListApiView.as_view(),name='api_vendor_list'),
    path('products/<str:pk>/',ProductDetailApiView.as_view(),name='api_vendor_detail'),
]