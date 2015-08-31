__author__ = 'K2A'
from django.db import models

from core.models import BaseModel
from user.models import UserProfile


class ProductCategory(BaseModel):
    name = models.CharField(max_length=255)
    image_url = models.CharField(max_length=255,blank=True,null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "category"

class ProductImage(BaseModel):
    url = models.CharField(max_length=255)

    def __unicode__(self):
        return self.url

    class Meta:
        db_table = "image"

class Look(BaseModel):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "look"

class Brand(BaseModel):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "brand"

class Product(BaseModel):
    # Stores all the activities

    LEVELS =  (
                ('1','Head'),
                ('2','Outer Wear'),
                ('3','Inner Wear'),
                ('4','Pant'),
                ('5','Shoe'),
                ('6','Accessories')
              )


    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.CharField(max_length=255, blank=True, default="")
    price_unit = models.CharField(max_length=255,blank=True,default="")
    link = models.CharField(max_length=255, blank=True, default="")  # link to the products in amazon
    primary_image_url = models.CharField(max_length=255,default="")  # url to static image files
    brand = models.ForeignKey(Brand,blank=True,null=True)
    images = models.ManyToManyField(ProductImage, blank=True)
    category = models.ManyToManyField(ProductCategory, blank=True)
    looks = models.ManyToManyField(Look, blank=True)
    level = models.CharField(max_length=255,choices=LEVELS)

    def __unicode__(self):
        return  self.name

    class Meta:
        db_table = "product"

    @property
    def likes(self):

        return ProductLikes.objects.filter(product = self).count()

    @property
    def get_category_str(self):
        category_objects = self.category.all()
        category_list = []
        for category in category_objects:
            category_list.append(category.name)
        return category_list

    @property
    def get_looks_str(self):
        looks_objects = self.looks.all()
        looks_list = []
        for looks in looks_objects:
            looks_list.append(looks.name)
        return looks_list


class ProductLikes(models.Model):
    product = models.ForeignKey(Product)
    user = models.ForeignKey(UserProfile)

    def __unicode__(self):
        return  self.name




    class Meta:
        db_table = "likes"


class Collection(BaseModel):
    user = models.ForeignKey(UserProfile)
    product1 = models.ForeignKey(Product,related_name="head",null=True)
    product2 = models.ForeignKey(Product,related_name="outer",null=True)
    product3 = models.ForeignKey(Product,related_name="inner",null=True)
    product4 = models.ForeignKey(Product,related_name="pant",null=True)
    product5 = models.ForeignKey(Product,related_name="shoe",null=True)
    product6 = models.ForeignKey(Product,related_name="accessory",null=True)

    def __unicode__(self):
        return  self.name

    class Meta:
        db_table = "collection"