# _*_ encoding:utf-8 _*_
date = '17-10-27 上午11:10'

from django.forms import forms
from .models import UploadModel


class UploadForm(forms.Form):
    headImg = forms.FileField()