from django.http.response import HttpResponse
from django.shortcuts import render

from .forms import UploadForm
from .models import UploadModel
# Create your views here.


def upload(request):
    if request.method == "POST":
        uf = UploadForm(request.POST, request.FILES)
        if uf.is_valid():
            headImg = uf.cleaned_data['headImg']
            user = UploadModel()
            user.img = headImg
            user.save()
            a = UploadModel.objects.all()
            return render(request,'upload.html',{'uf':uf,'upload':a})
    # else:
    #     uf = UploadForm()
    #     upload = UploadModel.objects.all()
    # return render(request,'upload.html',{'uf':uf,'upload':upload})
    else:
        uf = UploadForm()
        a = UploadModel.objects.all()
        return render(request, 'upload.html', {'uf': uf,'upload':a})