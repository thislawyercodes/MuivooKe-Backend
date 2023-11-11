from django.shortcuts import render
from rest_framework import generics,permissions
from api.models.customer_models import Customer,Order,OrderItem
from api.serializers.customer_serializers import  CustomerListSerializer,OrderListSerializer,OrderItemListSerializer

class CustomerListApiView(generics.ListCreateAPIView):
    permission_classes=[permissions.IsAuthenticated]
    queryset = Customer.objects.all()
    serializer_class=CustomerListSerializer

class CustomerDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[permissions.IsAuthenticated]
    queryset = Customer.objects.all()
    serializer_class=CustomerListSerializer

class OrderListApiView(generics.ListCreateAPIView):
    permission_classes=[permissions.IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class=OrderListSerializer    


class OrderDetailApiView(generics.ListAPIView):
    permission_classes=[permissions.IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class=OrderItemListSerializer   

    def get_queryset(self):
        order_id=self.kwargs['pk']
        order=Order.objects.get(id=order_id)
        orderItems=OrderItem.objects.filter(order=order)
        return orderItems


