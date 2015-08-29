# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('deleted_date', models.DateTimeField(null=True, blank=True)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'brand',
            },
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('deleted_date', models.DateTimeField(null=True, blank=True)),
                ('deleted', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'collection',
            },
        ),
        migrations.CreateModel(
            name='Look',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('deleted_date', models.DateTimeField(null=True, blank=True)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'look',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('deleted_date', models.DateTimeField(null=True, blank=True)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.CharField(default=b'', max_length=255, blank=True)),
                ('price_unit', models.CharField(default=b'', max_length=255, blank=True)),
                ('link', models.CharField(default=b'', max_length=255, blank=True)),
                ('primary_image_url', models.CharField(default=b'', max_length=255)),
                ('level', models.CharField(max_length=255, choices=[(b'1', b'Head'), (b'2', b'Outer Wear'), (b'3', b'Inner Wear'), (b'4', b'Pant'), (b'5', b'Shoe'), (b'6', b'Accessories')])),
                ('size', models.CharField(max_length=100, choices=[(b'S', b'S'), (b'M', b'M'), (b'L', b'L'), (b'XL', b'XL')])),
                ('brand', models.ForeignKey(blank=True, to='products.Brand', null=True)),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('deleted_date', models.DateTimeField(null=True, blank=True)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=255)),
                ('image_url', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('deleted_date', models.DateTimeField(null=True, blank=True)),
                ('deleted', models.BooleanField(default=False)),
                ('url', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'image',
            },
        ),
        migrations.CreateModel(
            name='ProductLikes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product', models.ForeignKey(to='products.Product')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'likes',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(to='products.ProductCategory', blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='images',
            field=models.ManyToManyField(to='products.ProductImage', blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='looks',
            field=models.ManyToManyField(to='products.Look', blank=True),
        ),
        migrations.AddField(
            model_name='collection',
            name='product1',
            field=models.ForeignKey(related_name='head', to='products.Product', null=True),
        ),
        migrations.AddField(
            model_name='collection',
            name='product2',
            field=models.ForeignKey(related_name='outer', to='products.Product', null=True),
        ),
        migrations.AddField(
            model_name='collection',
            name='product3',
            field=models.ForeignKey(related_name='inner', to='products.Product', null=True),
        ),
        migrations.AddField(
            model_name='collection',
            name='product4',
            field=models.ForeignKey(related_name='pant', to='products.Product', null=True),
        ),
        migrations.AddField(
            model_name='collection',
            name='product5',
            field=models.ForeignKey(related_name='shoe', to='products.Product', null=True),
        ),
        migrations.AddField(
            model_name='collection',
            name='product6',
            field=models.ForeignKey(related_name='accessory', to='products.Product', null=True),
        ),
    ]
