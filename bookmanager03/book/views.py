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
    