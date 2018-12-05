#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.cart),
    url(r'^delete$', views.delete),
    url(r'^change$', views.change),
    # url(r'^test$', views.test),
]