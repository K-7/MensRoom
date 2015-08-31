__author__ = 'vikas'
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from django.shortcuts import render
from django.template.defaultfilters import slugify
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

import json

from products.forms import ProductForm
from products.models import *
from utils.functions import generateGUID
from user.models import UserProfile



def home(request):
    context = {'items': Product.objects.all()}

    return render(
        request,
        'home.html',
        context
    )


def product_details(request, pid):

    context={}
    context['item'] = Product.objects.get(id=pid)
    return render (
                    request,
                    'product_details.html',
                    context
                  )

@user_passes_test(lambda u: u.is_superuser)
def forms(request):
    if request.POST:

        fileObj = request.FILES['image_url']
        file_name = u"{0}_{1}.jpg".format(slugify(fileObj.name), generateGUID())
        path = default_storage.save('product_images/' + file_name, ContentFile(fileObj.read()))

        print request.POST['looks']

        product = Product.objects.create(name=request.POST['name'])
        product.description = request.POST['description']
        product.price = request.POST['price']
        product.price_unit = request.POST['price_unit']
        product.link = request.POST['link']
        product.primary_image_url = file_name
        product.save()
        return HttpResponseRedirect('/')
    else:
        form = ProductForm()

    data = {}
    data.update(csrf(request))
    data['form'] = form
    return render(
        request,
        'product_form.html',
        data,
    )

@login_required
def preferences(request):

    context = {}
    context.update(csrf(request))
    context['brands'] = Brand.objects.all()

    return render(
        request,
        'preferences.html',
        context,
    )

@login_required
def search(request):

    context = {}
    context['category'] = ProductCategory.objects.all()
    return render(
        request,
        'search.html',
        context,
    )

@login_required
def trial_room(request):
    context = {}
    head = Product.objects.filter(level = '1')
    outerwear = Product.objects.filter(level = '2')
    innerwear = Product.objects.filter(level = '3')
    pants = Product.objects.filter(level = '4')
    shoes = Product.objects.filter(level = '5')

    context['head_zip'] = zip(range(head.count()), head)
    context['outerwear_zip'] = zip(range(outerwear.count()), outerwear)
    context['innerwear_zip'] = zip(range(innerwear.count()), innerwear)
    context['pants_zip'] = zip(range(pants.count()), pants)
    context['shoes_zip'] = zip(range(shoes.count()), shoes)
    return render(
        request,
        'trial_room.html',
        context,
        )


@login_required
def likes(request, pid):
    pid = int(pid)
    if request.GET:

        product = Product.objects.get(id=pid)

        try:
            ProductLikes.objects.get(product=product, user=request.user)
            return HttpResponse('Already Liked')
        except:
            pass

        ProductLikes.objects.create(product=product, user=request.user)
        return HttpReponse('Added to Likes')


@login_required
def collection(request,pid1,pid2,pid3,pid4,pid5,pid6):
    # item1 = Product.objects.get(id = pid1)
    item2 = Product.objects.get(id = pid2)
    item3 = Product.objects.get(id = pid3)
    item4 = Product.objects.get(id = pid4)
    item5 = Product.objects.get(id = pid5)
    # item6 = Product.objects.get(id = pid6)

    Collection.objects.create(
                                user = request.user,
                                product2 = item2,
                                product3 = item3,
                                product4 = item4,
                                product5 = item5,
                             )
    return HttpResponse("Added to Collections")


@login_required
def checkout(request,items):

    print "-----------------------------V2----------"
    list_items = []
    list_items = [x.encode('utf-8') for x in items.split('/')]
    items = []
    items = [int(x) for x in list_items if any(c.isdigit() for c in x)]
    checkout_items = []
    for i in items:
        print i
        item = Product.objects.get(id = i)
        checkout_items.append(item)

    context = {'items':checkout_items,}
    return render(
            request,
            'checkout.html',
            context,
            )


@login_required
def checkout_empty(request):

    return render (
                    request,
                    'checkout.html',
                  )


@login_required
def unlike(request,pid):


    pid = int(pid)
    like = ProductLikes.objects.get(product = pid, user = request.user)
    like.delete()
    msg = {'msg':'unliked'}
    return HttpResponse("yes")