from django.dispatch import receiver
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test

from allauth.socialaccount.models import SocialAccount
from allauth.account.signals import user_signed_up

from user.models import UserProfile
from products.models import *


def webapp(request):
    return HttpResponseRedirect("static/webapp/www/index.html")


def login(request):
    data = {}
    return render(
        request,
        'login.html',
        data
    )


@login_required
def user_profile(request):

    context={}
    likes = ProductLikes.objects.filter(user = request.user)
    collection = Collection.objects.filter(user = request.user)
    context['zip_likes'] = zip(range(likes.count()) ,likes )
    context['zip_collection'] = zip(range(collection.count()),collection)

    return render (
                    request,
                    'user_profile.html',
                    context
                  )


# saving profile picture before login
@receiver(user_signed_up)
def set_picture(sender,request, **kwargs):

    social_image=UserProfile.objects.latest('id')
    image = SocialAccount.objects.filter(provider = 'google', user = social_image.id)
    if image:
        pass
    else:
        image = SocialAccount.objects.filter(provider='facebook', user = social_image.id)
    if len(image):
        picture = image[0].get_avatar_url()
        try:
            social_image.avatar=picture
            social_image.save()
        except:
            pass
        return


