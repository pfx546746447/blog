# _*_ encoding:utf-8 _*_

from django.contrib import auth
from django.contrib.auth.hashers import make_password
import json

from django.db.models.query_utils import DeferredAttribute
from django.http.response import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from pure_pagination import Paginator, PageNotAnInteger, EmptyPage
from users.forms import LoginForm
from users.models import blogUser
from article.models import article, Collect


class HomePage(View):
    def get(self, request):
        # limit = 8  # 每页显示的记录数
        # topics = article.objects.all()
        # paginator = Paginator(topics, limit)  # 实例化一个分页对象
        #
        # page = request.GET.get('page')  # 获取页码
        # try:
        #     topics = paginator.page(page)  # 获取某页对应的记录
        # except PageNotAnInteger:  # 如果页码不是个整数
        #     topics = paginator.page(1)  # 取第一页的记录
        # except EmptyPage:  # 如果页码太大，没有相应的记录
        #     topics = paginator.page(paginator.num_pages)  # 取最后一页的记录
        # return render(request,'index.html', {'topics': topics})
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        topics = article.objects.all()
        # Provide Paginator with the request object for complete querystring generation
        p = Paginator(topics,8,request=request)
        articles = p.page(page)
        return render(request,'index.html', {'topics': articles})


class LoginView(View):
    @csrf_exempt
    def post(self, request):
        if request.method == 'POST':
            name = request.POST['user']
            pword = request.POST['password']
            user = auth.authenticate(username=name, password=pword)
            if user is not None:
                a = auth.login(request, user)
                return HttpResponse('{"status":"ok"}', content_type='application/json')
            else:
                return_json = {'status':'error','msg': 'username or password error'}
                return HttpResponse(json.dumps(return_json), content_type='application/json')


class RegistView(View):
    @csrf_exempt
    def post(self, request):
        if request.method == 'POST':
            name = request.POST['ruser']
            pwd = request.POST['rpassword']
            pwd2 = request.POST['rpassword2']
            if (pwd == pwd2):
                pwdd = make_password(pwd)
                try:
                    user = blogUser.objects.get_or_create(username=name, password=pwdd, name=name)
                    if user is not None:
                        return HttpResponse('{"status":"success","msg":"创建成功"}', content_type='application/json')
                except Exception, e:
                    print 'registError: ' + e
                    return HttpResponse('{"status":"error","msg":"用户已存在"}', content_type='application/json')
            else:
                return HttpResponse('{"status":"passError","msg":"密码不一致"}', content_type='application/json')


def logout(request):
    auth.logout(request)
    # return HttpResponseRedirect(reverse('homepage'))
    # 退出后直接返回到当前界面
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def clicks(request):
    if request.method == "POST":
        id = request.POST['id']
        article_ids = article.objects.get(id=id)
        article_ids.click += 1
        article_ids.save()
        print article_ids.click
        return HttpResponse('{"status":"ok"}', content_type='application/json')
