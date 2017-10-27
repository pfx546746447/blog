# _*_ encoding:utf-8 _*_
from django import forms

date = '17-10-17 上午10:19'


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)