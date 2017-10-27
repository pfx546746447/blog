"""MyBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from .views import *

urlpatterns = [
    url(r'^release$',ReleaseView.as_view(),name='release'),
    url(r'^collect$',CollectView.as_view(),name='collect'),
    url(r'^comment$',CommentView.as_view(),name='comment'),
    url(r'^article/(?P<pk>[0-9]+)/$', ArticleView.as_view(), name='article'),
]
