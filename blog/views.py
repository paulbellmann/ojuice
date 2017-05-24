# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def blogIndex(request):
    return render(request, 'index.html', {'title': 'Index', 'discription': 'index yo'})

def blogHund(request):
    return render(request, 'index.html', {'title': 'Test', 'discription': 'dies ist ein test'})