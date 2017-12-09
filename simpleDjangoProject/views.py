# -*- coding: utf-8 -*-

from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseNotFound

def index(request):
    return HttpResponse("hello world")