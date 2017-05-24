from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.blogIndex, name='index'),
    url(r'^test/$', views.blogHund, name='test'),
]