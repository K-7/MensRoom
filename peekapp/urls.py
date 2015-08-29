from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^app$', 'user.views.webapp'),
    url(r'^api/', include("api.urls")),
]

urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
   urlpatterns += [
       url(r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:],
       'django.views.static.serve',
       {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
       url(r'^%s(?P<path>.*)$' % settings.STATIC_URL[1:],
       'django.views.static.serve',
       {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
   ]


