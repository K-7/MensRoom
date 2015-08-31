from django.conf.urls import include, url
from products.views import *


urlpatterns = [

        url(r'^$',home),
        url(r'^index$',home),
        url(r'^form/$', forms),
        url(r'^preferences/$',preferences),
        url(r'^search/$',search),
        url(r'^article/(?P<pid>\d+)/$',product_details),
        url(r'^trial_room/$',trial_room),
        url(r'^collection/(?P<pid1>\d+)/(?P<pid2>\d+)/(?P<pid3>\d+)/(?P<pid4>\d+)/(?P<pid5>\d+)/(?P<pid6>\d+)/$',collection),
        url(r'^like/(?P<pid>\d+)/$',likes),
        url(r'^unlike/(?P<pid>\d+)/$',unlike),
        url(r'checkout/$', checkout_empty),
        url(r'checkout/(?P<items>.+)/$', checkout),
    ]