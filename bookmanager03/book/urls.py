from django.urls import path
from book.views import create_book, shop, register, json, response, set_cookie, get_cookie, set_session, get_session
from django.urls import converters
from django.urls.converters import register_converter
# 1.定义转换器
class MobileConverter:
    regex = r"1[3-9]\d{9}"
    # 验证没有问题的数据，给视图函数
    def to_python(self, value):
        return value

    # def to_url(self, value):
    #     return value、
# 2.先去注册转换器才可以使用
# def register_converter(converter, type_name)
# converter 转换器类    type_name 转换器，名字
register_converter(MobileConverter, 'phone')
urlpatterns = [
    path('create/', create_book),
    # <转换器名字：变量名>
    # 转换器会对变量数据进行正则的验证
    path('<int:city_id>/<phone:mobile>/', shop),
    path('register/',register),
    path('json/',json),
    path('res/',response),
    path('setcookie/',set_cookie),
    path('getcookie/',get_cookie),
    path('setsession/',set_session),
    path('getsession/',get_session),
]