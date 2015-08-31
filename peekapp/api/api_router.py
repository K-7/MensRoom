import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


@csrf_exempt
def router(request,api_version=1,operation=None):
    try:
        mod = __import__("api.api_version"+str(api_version),globals(),locals(),["ApiVersion"+str(api_version)])
        version_class = getattr(mod,"ApiVersion"+str(api_version))  
        if operation:
            return_obj = getattr(version_class(),operation)(request)
            return HttpResponse(return_obj)
        else:
            return_obj = {}             
            return_obj['status'] = "500"
            return_obj['reason_for_failure'] = "The specified Operation is not supported"
            return HttpResponse(json.dumps(return_obj))
    except Exception as e:  
        return_obj = {}
        return_obj['status'] = "500"
        return_obj['reason_for_failure'] = e
        return HttpResponse(json.dumps(return_obj))

