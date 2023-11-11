from rest_framework import serializers
from api.models.customer_models import Customer,Order,OrderItem



class CustomerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields="__all__"

    def __init__(self, *args, **kwargs):
        super(OrderListSerializer, self).__init__(*args,**kwargs)
        self.Meta.depth=1


   
class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields=["id","customer","order_time"]

    def __init__(self, *args, **kwargs):
        super(OrderListSerializer, self).__init__(*args,**kwargs)
        self.Meta.depth=1

class OrderItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields=["id","order","product"]

    def __init__(self, *args, **kwargs):
        super(OrderItemListSerializer, self).__init__(*args,**kwargs)
        self.Meta.depth=1
