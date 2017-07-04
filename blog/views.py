# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import Todo

# Create your views here.
def blogIndex(request):
    todos = Todo.objects.all()
    context = {
        'title': 'ToDos',
        'todos': todos
    }
    print request.session.session_key
    current_user = request.user
    print current_user.id
    return render(request, 'index.html', context)

def blogHund(request):
    return render(request, 'index.html', {'title': 'Test', 'discription': 'dies ist ein test'})

def details(request, todo_id):
    details = Todo.objects.get(pk=todo_id)
    context = {
        'title': 'Details',
        'discription': 'genauere hinweise',
        'details': details
    }

    return render(request, 'detail.html', context)

def new(request):
    context = {
        'title': 'Add new'
    } 
    return render(request, 'new.html', context)

def create_todo(request):
    todo = Todo()
    todo.title = request.GET['title']
    todo.body = request.GET['body']
    if todo.title and todo.body:
        todo.save()
    return redirect('index')

def del_todo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.delete()
    return redirect('index')

def modify_todo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.title = request.GET['title']
    todo.body = request.GET['body']
    todo.save()
    return redirect('index')

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
        return redirect('index')

def log_out(request):
    logout(request)
    return redirect('index')