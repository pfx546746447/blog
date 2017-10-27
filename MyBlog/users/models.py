# _*_ coding:utf-8 _*_

from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models
import django.utils.timezone as timezone


# Create your models here.


class blogUser(AbstractUser):
    name = models.CharField(max_length=20,verbose_name='用户名')
    tel = models.CharField(max_length=11,verbose_name='手机号',default='',blank=True)
    email = models.EmailField(verbose_name='邮箱')
    sex = models.CharField(max_length=5,choices=(('man','男'),('woman','女')),verbose_name='性别')
    img = models.ImageField(max_length=200,upload_to='avatar/%Y/%m/',blank=True,null=True,verbose_name='头像')
    time = models.DateTimeField(default=timezone.now,verbose_name='添加时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
