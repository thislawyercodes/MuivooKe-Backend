from rest_framework import serializers
from api.models.vendor_models import Vendor


class VendorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields="__all__"

    def __init__(self, *args, **kwargs):
        super(VendorListSerializer, self).__init__(*args,**kwargs)
        self.Meta.depth=1

