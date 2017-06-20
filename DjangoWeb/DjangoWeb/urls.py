"""DjangoWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from DjangoWeb.view import hello
from DjangoWeb.settings import STATIC_URL
import os,settings

urlpatterns = [
    url(r'^$','DjangoWeb.view.login'),
    url(r'^hello/plus/(\d{1,2})/(\d{1,3})/$','DjangoWeb.view.hello_plus'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$','DjangoWeb.view.home'),
    url(r'^index/$','DjangoWeb.view.index'),
    url(r'^index/(\w+)/$','DjangoWeb.view.testArgs'),
    url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_URL}),
    # url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_URL}),
    # url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_URL}),
]
