# -*- coding: utf-8 -*-

from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseNotFound
from django.shortcuts import render
from django.utils import timezone
from django.db.models import F

import json,datetime,hashlib,decimal

def index(request):
    return render(request, 'index.html', locals())
