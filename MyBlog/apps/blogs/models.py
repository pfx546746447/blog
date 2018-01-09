# _*_ coding:utf-8 _*_

from django.db import models
from datetime import datetime
from DjangoUeditor.models import UEditorField

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=50,verbose_name='标题')
    body = UEditorField(verbose_name='内容',width=600, height=300, imagePath="uedirotImg", filePath="ueditorFile",default="")
    click = models.IntegerField(default=0,verbose_name="点击数")
    add_time = models.DateField(default=datetime.now(),verbose_name="添加时间")

    class Meta:
        verbose_name = "博客"
        verbose_name_plural = verbose_name