#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.conf.urls import  url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^list(\d*)/(\d*)$', views.list),
    url(r'^detail(\d+)', views.detail),
    url(r'^getsession/$',views.getsession),
    url(r'^send/$',views.send),
]