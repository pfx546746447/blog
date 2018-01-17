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
        blogs = Blog.objects.all()
        category = Category.objects.all()
        tag = Tags.objects.all()
        return render(request, 'blog-desc.html',
                      {"blog": blog,
                       'blog_num': blogs.count(),
                       'category_num': category.count(),
                       'tag_num': tag.count(),
                       'categorys': category})


def add_click(request):
    id = request.POST.get('id', '')
    blog = Blog.objects.get(id=int(id))
    blog.click += 1
    blog.save()
    return HttpResponse('{"status":"success"}', content_type="application/json")


class ArchiveView(View):
    def get(self,request):
        blogs = Blog.objects.all().order_by('-add_time')
        try:
            page = request.GET.get('page', 1)

        except PageNotAnInteger:
            page = 1

        # Provide Paginator with the request object for complete querystring generation

        p = Paginator(blogs, 15)
        blogs = p.page(page)

        blog = Blog.objects.all()
        category = Category.objects.all()
        tag = Tags.objects.all()
        return render(request,'archive.html',{'blogs':blogs})
