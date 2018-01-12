# _*_ coding:utf-8 _*_

from django.db import models
from datetime import datetime
from django.utils import timezone
from DjangoUeditor.models import UEditorField


# from django.utils.timezone import utc

# now = datetime.utcnow().replace(tzinfo=utc)


# Create your models here.

class Tags(models.Model):
    # blog = models.ManyToManyField(Blog, verbose_name='博客')
    name = models.CharField(default="", blank=True, max_length=50, verbose_name='标签')
    add_time = models.DateTimeField(default=timezone.now, verbose_name="添加时间")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name


class Category(models.Model):
    # blog = models.ManyToManyField(Blog, verbose_name='博客')
    name = models.CharField(default="", blank=True, max_length=50, verbose_name='标签')
    add_time = models.DateTimeField(default=timezone.now, verbose_name="添加时间")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = verbose_name


class Blog(models.Model):
    title = models.CharField(max_length=50, verbose_name='标题')
    body = UEditorField(verbose_name='内容', width=600, height=300, imagePath="uedirotImg", filePath="ueditorFile")
    tags = models.ManyToManyField(Tags, verbose_name='标签')
    category = models.ManyToManyField(Category, verbose_name='分类')
    type = models.CharField(choices=(('yc','原创'),('zz','转载')),max_length=4,default="yc")
    click = models.IntegerField(default=0, verbose_name="点击数")
    add_time = models.DateTimeField(default=timezone.now, verbose_name="添加时间")

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "博客"
        verbose_name_plural = verbose_name
