# _*_encoding:utf-8 _*_

from pure_pagination import Paginator,PageNotAnInteger,EmptyPage
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from users.models import blogUser
from .models import *

class ReleaseView(View):
    def get(self,request):
        return render(request,'release.html')
    @csrf_exempt
    def post(self,request):
        if request.method == 'POST':
            title = request.POST['title']
            desc = request.POST['desc']
            body = request.POST['body']
            username = request.POST['username']
            users = blogUser.objects.filter(username=username)
            text = article()
            for user in users:
                id = user.id
                text.title = title
                text.desc = desc
                text.body = body
                text.user_id = id
                text.category_id = 1
                text_save = text.save()
                if text_save is None:
                    return HttpResponse('{"status":"success"}', content_type="application/json")
                else:
                    return HttpResponse('{"status":"error"}', content_type="application/json")


class CollectView(View):
    def post(self,request):
        if request.user.is_authenticated():
            userId = request.POST['userId']
            articleId = request.POST['articleId']
            print userId+":::"+articleId
            collectNum = article.objects.get(id=articleId)
            collected = Collect.objects.filter(user_id=userId, articles_id=articleId,has_collect=True)
            if len(collected) > 0:
                collected.delete()
                collectNum.click -= 1
                collectNum.save()
                return HttpResponse('{"status":"noCollect"}',content_type='application/json')
            else:
                Collect.objects.get_or_create(user_id=userId,articles_id=articleId,has_collect=True)
                collectNum.collect += 1
                collectNum.save()
                return HttpResponse('{"status":"Collect"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"noLogin"}',content_type='application/json')

class ArticleView(View):
    def get(self,request,pk):
        articles = article.objects.filter(pk=pk)
        collect = Collect.objects.filter(articles_id=pk)
        topics = Comment.objects.filter(articles_id=pk)
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        # Provide Paginator with the request object for complete querystring generation
        p = Paginator(topics,8,request=request)
        articless = p.page(page)
        print 'articless'
        print len(topics)
        print 'articless'
        if collect is None:
            if len(topics) == 0:
                return render(request,'article.html',{'article':articles,'collect':'','topics':''})
            else:
                return render(request, 'article.html', {'article': articles, 'collect': '', 'topics': articless})
        else:
            if len(topics) == 0:
                return render(request, 'article.html', {'article': articles, 'collect': collect,'topics':''})
            else:
                return render(request, 'article.html', {'article': articles, 'collect': collect, 'topics': articless})

class CommentView(View):
    def post(self,request):
        userId = request.POST['userId']
        articleId = request.POST['articleId']
        comment = request.POST['comment']
        comm = Comment(user_id=userId,articles_id=articleId,text=comment)
        comm.save()
        return HttpResponse('{"status":"ok"}', content_type='application/json')