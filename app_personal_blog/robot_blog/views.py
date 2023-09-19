#
#
#
#
#
from django.http import HttpResponse


def hi_world_view(request):
    html_response = "<h1>Hi world</h1>"
    return HttpResponse(html_response)
