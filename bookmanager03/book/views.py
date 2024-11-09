from django.http import HttpResponse
from django.shortcuts import render
from book.models import BookInfo
# Create your views here.

# 增加
def create_book(request):
    book=BookInfo.objects.create(
        name='abc',
        pub_date='2000-01-01',
        readcount=10
    )
    return HttpResponse('create')

def shop(request,city_id,shop_id):
    # print(city_id,shop_id)
    query_params = request.GET.get('order')
    print(query_params)
    # http://localhost:8000/10010/10011/?order=readcount
    # ?后面是get请求方式
    # 打印结果：readcount
    return HttpResponse('齐哥的小饭店')

def register(request):
    data=request.POST
    print(data)
    return HttpResponse('ok')