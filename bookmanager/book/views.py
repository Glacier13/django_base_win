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

    # 1.return HttpResponse('ok')
    # 2.return render(request, 'book/index.html')
    # render 渲染模版
    # render参数:request 请求, template_name 模版名字, context=None 将视图中的数据传给html(模板)
    # 3.模拟数据查询
    # context=  1)将视图中的数据传给html(模板)
    # 2) html(模板)采用{{ 变量 }} 形式来展示数据
    context = {
        'name': '马上双十一，点击有惊喜'
    }
    return render(request, 'book/index.html',context=context)