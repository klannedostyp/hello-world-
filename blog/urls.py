from django.conf.urls import include, url
from django.contrib import admin
from django.views import *
from . import views

urlpatterns= [
     # url(r'^$', views.index, name='index'),
      url(r'^admin', include(admin.site.urls)),
     # url(r'^$', views.post_list, name='post_list'),
     # url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
     # url(r'^post/new/$', views.post_new, name='post_new'),
     # url(r'^$', main, name='index'),
     # url(r'^works/$', works, name='works'),
     # url(r'^learns/$', learn, name='learns'),
     # url(r'^organization/(\d+)/$', organization, name='organization'),
     # url(r'^get_works/$', get_works),
]