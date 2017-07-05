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
    if not request.user.is_authenticated:
        return render(request, 'login.html', context)
    else:
        return redirect('index')

def log_on(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        messages.add_message(request, messages.SUCCESS, "You are now logged in.")
        return redirect('index')
    else:
        messages.add_message(request, messages.WARNING, "Password or Username is wrong.")
        return redirect('login')

@login_required
def log_out(request):
    logout(request)
    messages.add_message(request, messages.INFO, "Succesfully logged out.")
    return redirect('index')