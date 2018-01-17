# _*_encoding:utf-8_*_

from django.shortcuts import render
from django.views.generic import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from blogs.models import *


# Create your views here.

class IndexView(View):
    def get(self, request):
        blogs = Blog.objects.all().order_by("-add_time")

        try:
            page = request.GET.get('page', 1)

        except PageNotAnInteger:
            page = 1

        # Provide Paginator with the request object for complete querystring generation

        p = Paginator(blogs, 10)
        blogs = p.page(page)

        blog = Blog.objects.all()
        category = Category.objects.all()
        tag = Tags.objects.all()

        return render(request, 'center-blog.html',
                      {"blogs": blogs,
                       'blog_num': blog.count(),
                       'category_num': category.count(),
                       'tag_num': tag.count(),
                       'categorys': category})
