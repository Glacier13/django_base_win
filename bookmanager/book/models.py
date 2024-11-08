from django.db import models
"""
    1.我们的模型需要继承自models.Model
    2.系统自动添加主键--id
    3.字段
        字段名=model.类型（选项）
        字段名其实就是数据表的属性
        字段名不要使用python，mysql关键字
"""
# Create your models here.
class BookInfo(models.Model):
    # id
    name = models.CharField(max_length=10)

    # 重写str方法，以显示书籍名字
    def __str__(self):
        return self.name

class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    # 外键约束：人类属于哪本书
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)