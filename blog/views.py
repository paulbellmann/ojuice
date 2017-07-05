# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Todo


def blogIndex(request):
    #todos = Todo.objects.all()
    if request.user.is_authenticated:
        todos = Todo.objects.filter(owner=request.user.id)
        context = {
            'title': 'Todos',
            'todos': todos
        }
        print request.session.session_key
        current_user = request.user
        print current_user.id
        return render(request, 'index.html', context)
    else:
        print 'nicht logged in'
        return redirect('login')

@login_required
def details(request, todo_id):
    details = Todo.objects.get(pk=todo_id)
    context = {
        'title': 'Details',
        'discription': 'genauere hinweise',
        'details': details
    }

    return render(request, 'detail.html', context)

@login_required
def new(request):
    context = {
        'title': 'Add new'
    } 
    return render(request, 'new.html', context)

@login_required
def create_todo(request):
    todo = Todo()
    if int(request.GET['quick']) == 1 and '#' in request.GET['title']:
        todo.title = request.GET['title'].split("#")[1].split(" ")[0]
        todo.body = request.GET['title'].split(" ", 1)[1]
    else:
        todo.title = request.GET['title']
        todo.body = request.GET['body']
    todo.owner = request.user
    if todo.title and todo.body:
        todo.save()
    return redirect('index')

@login_required
def del_todo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    if request.user == todo.owner:
        todo.delete()
    return redirect('index')

@login_required
def modify_todo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.title = request.GET['title']
    todo.body = request.GET['body']
    if request.user == todo.owner:
        todo.save()
    return redirect('index')

@login_required
def change_checked(request):
    todo = Todo.objects.get(pk=request.GET['ID'])
    print todo.checked
    todo.checked = not todo.checked
    print todo.checked
    if request.user == todo.owner:
        todo.save()
    #return redirect('index')