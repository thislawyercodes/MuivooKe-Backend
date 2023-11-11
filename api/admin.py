from django.contrib import admin
from api.models.vendor_models import Vendor
from api.models.product_models import Product,ProductCategory
from api.models.customer_models import Customer,Order,OrderItem
from api.models.review_models import ProductReviews


admin.site.register(Vendor)
admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ProductReviews)


