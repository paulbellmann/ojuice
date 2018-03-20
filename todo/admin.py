# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Todo, Rel

# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'body', 'created_at')

class RelAdmin(admin.ModelAdmin):
    list_display = ('rel', 'count', 'created_at')


admin.site.register(Todo, TodoAdmin)
admin.site.register(Rel, RelAdmin)
