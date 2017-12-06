# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    response = "Display all the list of users" 
    return HttpResponse(response)

def register(request):
    response = "Create a new user record" 
    return HttpResponse(response)

def login(request):
    response = "Login page for users" 
    return HttpResponse(response)