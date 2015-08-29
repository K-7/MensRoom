from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^app$', 'user.views.webapp'),
    url(r'',include('products.urls')),
    url(r'^accounts/', include('allauth.urls')),
]


