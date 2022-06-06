from django.shortcuts import render

# Create your views here.
'''
所谓的视图，就是由python函数编写的
视图函数有两个要求：
   1.接收请求
   2.返回一个响应
'''
from django.http import HttpRequest
from django.http import HttpResponse

# 期望用户输入 http://127.0.0.1:8000/index/
# 来访问视图函数


def index(request):
    return HttpResponse('ok')
