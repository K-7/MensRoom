from django.contrib import admin
from products.models import Product,Collection,ProductLikes,\
    Brand,Look,ProductImage,ProductCategory

admin.site.register(ProductCategory)
admin.site.register(ProductImage)
admin.site.register(Look)
admin.site.register(Brand)
admin.site.register(ProductLikes)
admin.site.register(Collection)
admin.site.register(Product)
