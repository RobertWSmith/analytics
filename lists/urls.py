# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 21:23:17 2014

@author: A421356
"""

from django.conf.urls import patterns, url

from lists import views

urlpatterns = patterns(
    '',
    url(r'^$', views.home_page, name='index'),
   )