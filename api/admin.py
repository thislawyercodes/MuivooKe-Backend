from django.contrib import admin
from api.models.vendor_models import Vendor
from api.models.product_models import Product,ProductCategory

admin.site.register(Vendor)
admin.site.register(Product)
admin.site.register(ProductCategory)

