# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from blog.models import Todo

def register(request):
    if request.method == 'POST':
        if User.objects.filter(username=request.POST['username']).exists():
            messages.add_message(request, messages.WARNING, "Username is already in use.")
            return redirect('register')
        user = User.objects.create_user(
            request.POST['username'],
            None,
            request.POST['password']
            )
        todo = Todo.objects.create(
            title ='Add Todo', body ='Try either Add new or quick todo',
            owner = user
        )
        todo = Todo.objects.create(
            title ='Share', body ='Tell your friends about ojuice!',
            owner = user
        )
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        login(request, user)
        messages.add_message(request, messages.SUCCESS, "Your Account got created.")
        return redirect('index')
    else:
        if not request.user.is_authenticated:
            context = {
                'title': 'Register'
            }
            return render(request, 'register.html', context)
        else:
            messages.add_message(request, messages.WARNING, "First you need to log out.")
            return redirect('index')

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