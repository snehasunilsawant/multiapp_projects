# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    context= {
            "word": get_random_string(length=14),
            } 
    try:
        request.session['count'] +=1

    except:
        request.session['count'] = 1
          
    return render(request,'randomword_app/index.html',context)