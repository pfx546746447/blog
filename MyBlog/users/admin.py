from django.contrib import admin

from models import *
# Register your models here.

class UserRegist(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(blogUser,UserRegist)
