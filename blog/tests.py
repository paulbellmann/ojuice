# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from .models import Todo

class BlogViewsTestCase(TestCase):
    """tests blog app"""
    def test_index(self):
        resp = self.client.get('/blog/')
        self.assertEqual(resp.status_code, 302)

    def test_create_todo(self):
        todo = Todo.objects.create(
            title='Do sports',
            body='Tests this Todo-Body',
            owner=1
        )
        self.assertEqual(todo, Todo.objects.get(title='Do sports'))