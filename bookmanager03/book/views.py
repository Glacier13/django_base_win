from django.http import HttpResponse,JsonResponse
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

def shop(request,city_id,mobile):

    """
    1.正则验证商品ID
    import re
    if not re.match('\d{5}',shop_id):
        return HttpResponse('error')
    """

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

def json(request):
    # json数据不能通过request.POST获取
    body=request.body
    # print(body)
    # b'{\r\n    "name":"itcast",\r\n    "age":10\r\n\r\n}'
    body_str=body.decode()
    # print(body_str)
    # {
        # "name":"itcast",
        # "age":10
    # }
    # print(type(body_str))
    """
    json形式的字符串可以转换成Python的字典
    """
    import json
    body_dict=json.loads(body_str)
    # print(body_dict)

    """
    请求头
    """
    # print(request.META)
    print(request.META['SERVER_PORT'])
    return HttpResponse('ok')

def response(request):
    # json --> dict
    # dict --> JSON

    """
    safe = True 是表示data是字典数据
    JsonResponse 可以把字典转换为Json
    现在给了一个非字典数据，出了问题我们自己负责safe=False

    json.loads --> json字符串转换为字典
    json.dumps --> 将字典转换为字符串
    """
    # 字典列表，传递一个列表
    info = [
        {'name': 'itcast',
         'address': 'shunyi'
         },
        {
        'name': 'heima',
        'address': 'beijing'
        }
    ]
    # data返回的相应数据，一般是字典类型
    response = JsonResponse(data=info,safe=False)
    # print(type(response))
    return response
    # return HttpResponse('res',status=200)
    # 1xx
    # 2xx
    #   200 成功
    # 3xx
    # 4xx 请求有问题
    #   404 找不到页面，路由有问题
    #   403 禁止访问，权限问题
    # 5xx

def set_cookie(request):
    # http://127.0.0.1:8000/setcookie/?username=itcast&password=123
    username=request.GET.get('username')
    response = HttpResponse('set_cookie')
    response.set_cookie('name',username,max_age=3600)
    # max_age为有效时间。单位为秒

    # 删除cookie
    response.delete_cookie('name')
    return response

def get_cookie(request):
    # request.COOKIES字典数据
    name=request.COOKIES.get('name')
    return HttpResponse(name)

"""
    第一次请求http://127.0.0.1:8000/set_session/?username=itheima 。我们在服务器端设置session信息
    服务器同时会生成一个sessionid的cookie信息。
    浏览器接收到这个信息之后，会把cookie数据保存起来
    第二次及其之后的请求 都会携帝这个sessionid，服务器会验证这个sessionid，验证没有问题会读取相关数据·实现业务逻辑
"""
def set_session(request):
    # 1、模拟 获取用户信息
    username=request.GET.get('username')
    # 2.设置session信息
    # 假如 我们通过模型查询 查询到了 用户的信息user_id = 1
    user_id = 1
    request.session['user_id']=user_id
    request.session['username']=username
    return HttpResponse('set_session')

def get_session(request):
    # 127.0.0.1:8000/setsession/?username=itheima
    # user_id=request.session['user_id']
    # username=request.session['username']
    # 不报错：
    user_id = request.session.get('user_id')
    username = request.session.get('username')

    content=f'{user_id},{username}'

    return HttpResponse(content)