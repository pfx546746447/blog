from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from users.views import blogUser
from .forms import UploadForm

class UserInfoView(View):
    def get(self,request):
        user = blogUser.objects.filter(id=request.user.id)
        return render(request,'userInfo.html',{'user':user,'active':'info'})

    @csrf_exempt
    def post(self,request):
        upload_form = UploadForm(request.POST,request.FILES)
        if upload_form.is_valid():
            img = upload_form.cleaned_data['headImg']
            print img
            users = blogUser.objects.filter(id=request.user.id)
            users.update(img=img)

            userBlog = blogUser.objects.filter(id=request.user.id)
            return render(request,'userInfo.html',{'user':userBlog,'active':'info'})