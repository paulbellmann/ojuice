# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def log_in(request):
    context = {
        'title': 'Log In'
    } 
    return render(request, 'login.html', context)

def log_on(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        messages.add_message(request, messages.SUCCESS, "Successfully logged in.")
        return redirect('index')
    else:
        messages.add_message(request, messages.WARNING, "Wrong Password or Username!")
        return redirect('login')

@login_required
def log_out(request):
    logout(request)
    return redirect('index')