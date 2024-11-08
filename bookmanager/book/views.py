from django.shortcuts import render

# Create your views here.
"""
视图就是python函数
视图有两个要求：
        1.视图函数的第一个参数就是接受请求
        2.必须返回一个相应
"""
from django.http import HttpRequest
from django.http import HttpResponse

def index(request):

    return HttpResponse('ok')