from django.conf.urls import url, include
from blogs.models import *
from blogs.views import *

urlpatterns = [
    url(r'desc/(?P<blogId>\d+)', BlogDescView.as_view(), name="blogDesc"),
    url(r'desc/add_click', add_click, name='add_click'),
    url(r'archive', ArchiveView.as_view(), name='archive'),
    url(r'category/(?P<categoryId>\d+)', CategoryAndTagView.as_view(), name='category'),
]
