from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.todoIndex, name='index'),
    url(r'^new/', views.new, name='new'),
    url(r'^create/', views.create_todo, name='create'),
    url(r'^create_quick/', views.create_quick_todo, name='create_quick'),
    url(r'^detail/(?P<todo_id>\d+)/$', views.details, name='detail'),
    url(r'^modify/(?P<todo_id>\d+)/$', views.modify_todo, name='modify'),
    url(r'^delete/(?P<todo_id>\d+)/$', views.del_todo, name='delete'),
    url(r'^change_checked/', views.change_checked, name='change_checked'),
]