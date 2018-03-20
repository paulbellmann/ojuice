# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from hashid_field import HashidAutoField


class Todo(models.Model):
    title = models.CharField(max_length=30)
    body = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    checked = models.BooleanField(default=False)
    # owner = models.ForeignKey(User, on_delete=models.CASCADE)
    owner = models.ManyToManyField(User)
    id = HashidAutoField(primary_key=True)

    def __str__(self):
        return "%s: %s" % (self.title, self.body)

class Rel(models.Model):
    rel = models.CharField(max_length=30)
    count = models.SmallIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def countUp(self):
        self.count += 1
        self.save()