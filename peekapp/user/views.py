from django.http import HttpResponseRedirect


def webapp(request):
    return HttpResponseRedirect("/site_media/static/webapp/www/index.html")
