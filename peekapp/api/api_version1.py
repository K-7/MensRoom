
import json
from datetime import datetime,date

from products.models import *

#version 1
class ApiVersion1():

    #login
    def login(self, request):
        print "===================="
        try:
            return_obj  ={}
            attrs = json.loads(request.body)

            category_list = []
            for category in ProductCategory.objects.all():
                obj = {}
                obj['name'] = category.name
                obj['url'] = category.image_url
                category_list.append(obj)

            brand_list = []
            for brand in Brand.objects.all():
                brand_list.append(brand.name)

            look_list = []
            for look in Look.objects.all():
                look_list.append(look.name)

            product_list = []
            for product in Product.objects.all():
                obj = {}
                obj['id'] = product.id
                obj['name'] = product.name
                obj['description'] = product.description
                obj['price'] = product.price
                obj['price_unit'] = product.price_unit
                obj['link'] = product.link
                obj['image_url'] = "http://dev.joyage.in/site_media/media/product_images/"+product.primary_image_url
                obj['brand'] = product.brand.name
                obj['category'] = product.get_category_str
                obj['looks'] = product.get_looks_str
                obj['level'] = product.level
                product_list.append(obj)

            return_obj['product_list'] = product_list
            return_obj['category_list'] = category_list
            return_obj['brand_list'] = brand_list
            return_obj['look_list'] = look_list
            return_obj['status'] = "1"
        except Exception as e:
            print e
            print "+++++++++"
            return_obj['status'] = '500'
            return_obj['reason_for_failure'] = "Failed sorry !!"
        return json.dumps(return_obj)

