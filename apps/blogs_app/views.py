# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    response = "Display all the list of blogs"
    return HttpResponse(response)

def new(request):
    response = "A new form to create a new blog"
    return HttpResponse(response)

def create(request):
   return redirect('/blogs')

def show(request,number):
    response = "Display Blog No : {}".format(number)
    return HttpResponse(response)

def edit(request,number):
    response = "Edit Blog No : {}".format(number)
    return HttpResponse(response)

def delete(request,number):
    return redirect('/blogs')