from django.urls import path 
from .views.vendor_views import VendorListApiView,VendorDetailApiView
from .views.product_views import ProductListApiView,ProductDetailApiView
from .views.customer_views import CustomerListApiView,CustomerDetailApiView,OrderDetailApiView,OrderListApiView
from .views.product_review_views import ProductReviewListApiView,ProductReviewDetailApiView


app_name = 'api'

urlpatterns =[
    path('vendors',VendorListApiView.as_view(),name='api_vendor_list'),
    path('vendors/<str:pk>/',VendorDetailApiView.as_view(),name='api_vendor_detail'),
    path('products',ProductListApiView.as_view(),name='api_vendor_list'),
    path('products/<str:pk>/',ProductDetailApiView.as_view(),name='api_vendor_detail'),
    path('customers',CustomerListApiView.as_view(),name='api_customer_list'),
    path('customers/<str:pk>/',CustomerDetailApiView.as_view(),name='api_customer_detail'),
    path('orders',OrderListApiView.as_view(),name='api_customer_list'),
    path('orders/<str:pk>/',OrderDetailApiView.as_view(),name='api_customer_detail'),
    path('reviews',ProductReviewListApiView.as_view(),name='api_reviews_list'),
    path('reviews/<str:pk>/',ProductReviewDetailApiView.as_view(),name='api_reviews_detail')
]
