from django.shortcuts import render

from products.models import Product

def home(request):

    context = {}
    context['data'] = Product.objects.all()
    return render (
                    request,
                    'home.html',
                    context
                    )