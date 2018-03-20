# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required

from .forms import TodoForm, QuickTodoForm
from .models import Todo, Rel


def todoIndex(request):
    rel = request.GET.get('rel', '')
    if rel:
        rels = Rel.objects.filter(rel=rel)
        if rels:
            rels.first().countUp()
        else:
            Rel.objects.create(rel=rel)

    ua = request.META.get('HTTP_USER_AGENT', '').lower()
    if ua.find("iphone") > 0 or ua.find("ipad") > 0 or ua.find("android") > 0:
        mobile = True
    else:
        mobile = False
    if request.user.is_authenticated:
        todos = Todo.objects.filter(owner=request.user)
        form = QuickTodoForm()
        context = {
            'title': 'Todos',
            'todos': todos,
            'form': form,
            'mobile': mobile
        }
        return render(request, 'index.html', context)
    else:
        return redirect('login')


@login_required
def details(request, todo_id):
    details = Todo.objects.get(pk=todo_id)
    context = {
        'title': 'Details',
        'details': details
    }
    if request.user.todo_set.filter(pk=todo_id).exists():
        return render(request, 'detail.html', context)
    else:
        return redirect('index')


@login_required
def create_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            a1 = Todo(
                title=form.cleaned_data['title'],
                body=form.cleaned_data['body']
            )
            a1.save()
            a1.owner.add(request.user)
        return redirect('index')
    else:
        form = TodoForm()
        context = {
            'title': 'Add new',
            'form': form
        }
        return render(request, 'new.html', context)


@login_required
def create_quick_todo(request):
    form = QuickTodoForm(request.POST)
    if form.is_valid():
        try:
            title = form.cleaned_data['title'].split(" ")[0]
            body = form.cleaned_data['title'].split(" ", 1)[1]
        except IndexError:
            title = form.cleaned_data['title']
            body = ''
        a1 = Todo(
            title=title,
            body=body
        )
        a1.save()
        a1.owner.add(request.user)
    return redirect('index')


@login_required
def del_todo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    if request.user.todo_set.filter(pk=todo_id).exists():
        todo.delete()
    return HttpResponse("OK")


@login_required
def modify_todo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.title = request.GET['title']
    todo.body = request.GET['body']
    if request.user.todo_set.filter(pk=todo_id).exists():
        todo.save()
    else:
        print "lol"
    return redirect('index')


@login_required
def change_checked(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.checked = not todo.checked
    if request.user.todo_set.filter(pk=todo_id).exists():
        todo.save()
    return HttpResponse("OK")

@login_required
def accept_invite(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.owner.add(request.user)
    return HttpResponse("OK")
