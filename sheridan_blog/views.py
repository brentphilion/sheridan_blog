# mysite/views.py

from django.http import HttpResponse


def index(request):
    return HttpResponse('Is this thing on?  this is the sheridan_blog project')