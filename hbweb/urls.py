from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('hbweb.views',
    url(r'^$', 'index')
)
