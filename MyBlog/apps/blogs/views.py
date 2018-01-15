# _*_encoding:utf-8_*_
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from .models import *


# Create your views here.

class BlogDescView(View):
    def get(self, request, blogId):
        blog = Blog.objects.get(id=blogId)
        return render(request, 'blog-desc.html', {"blog": blog})


def add_click(request):
    id = request.POST.get('id','')
    blog = Blog.objects.get(id=int(id))
    is_click = request.POST.get('is_click', '')
    print is_click
    if is_click == 'true':
        blog.click += 1
        blog.save()
    return HttpResponse('{"status":"success"}', content_type="application/json")
