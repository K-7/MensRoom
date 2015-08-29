from django.conf.urls import patterns, url
from api import api_router

urlpatterns = patterns("",
    
    url(r'^(?P<api_version>\d)/(?P<operation>\w+)$', api_router.router, name='api_router'),

)