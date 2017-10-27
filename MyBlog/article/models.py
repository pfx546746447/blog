# _*_ encoding:utf-8 _*_

from __future__ import unicode_literals

from django.db import models
from datetime import datetime
import django.utils.timezone as timezone

from users.models import blogUser
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50,verbose_name='名称')
    time = models.DateTimeField(auto_now_add=True,verbose_name='添加时间')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

class article(models.Model):
    user = models.ForeignKey(blogUser)
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=50,verbose_name='标题')
    desc = models.CharField(max_length=400,verbose_name='描述')
    body = models.TextField(verbose_name='主体内容')
    click = models.IntegerField(default=0,verbose_name='点击数')
    collect = models.IntegerField(default=0,verbose_name='收藏数')
    time = models.DateTimeField(default=datetime.now().strftime("%Y-%m-%d %H:%I:%S"),verbose_name='发布时间')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

class Collect(models.Model):
    user = models.ForeignKey(blogUser,related_name='collect_user',verbose_name='收藏用户')
    articles = models.ForeignKey(article,related_name='collect_article',verbose_name='收藏文章')
    has_collect = models.BooleanField(default=False,verbose_name='是否收藏')

    class Meta:
        verbose_name = '收藏'
        verbose_name_plural = verbose_name


class Comment(models.Model):
    user = models.ForeignKey(blogUser,related_name='comment_user',verbose_name='评论用户')
    articles = models.ForeignKey(article,related_name='comment_article',verbose_name='评论文章')
    text = models.TextField(verbose_name='评论内容')
    time = models.DateTimeField(default=datetime.now,verbose_name='评论时间')

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name
        db_table = 'Comment'