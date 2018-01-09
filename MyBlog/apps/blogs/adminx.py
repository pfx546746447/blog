# _*_coding:utf-8_*_
from django.core.files.storage import FileSystemStorage

import xadmin
from .models import *
from tools.widgets import Ueditor
import os
from MyBlog import settings


class blogAdmin(object):
    style_fields = {"body": "ueditor"}


xadmin.site.register(Blog, blogAdmin)
