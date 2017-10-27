# _*_ encoding:utf-8 _*_
from django.forms import forms

from users.models import blogUser

date = '17-10-27 上午9:33'


class UploadForm(forms.Form):
    headImg = forms.FileField()