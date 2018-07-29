"""crudapp URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from blog_posts import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog_posts/', include('blog_posts.urls', namespace='blog_posts')),
    url(r'^$',views.post_list,name='post_list'),
    url(r'^$',views.post_list,name='post_create'),
    url(r'^$',views.post_list,name='post_update'),
    url(r'^$',views.post_list,name='post_delete'),
    url(r'^$',views.index,name='index'),
    url(r'^formpage/',views.form_name_view,name='form_name_view'),
]