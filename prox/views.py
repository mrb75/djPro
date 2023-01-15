from django.shortcuts import render
from django.views.decorators.http import require_http_methods
import urllib
# Create your views here.





@require_http_methods(["GET", "POST","PATCH","PUT","DELETE"])
def guide(request):
    uri = request.build_absolute_uri()
    res = urllib.request.urlopen(uri)
    return res
    
    
