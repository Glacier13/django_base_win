from django.db import models
"""
    1.我们的模型需要继承自models.Model
    2.系统自动添加主键--id
    3.字段
        3-1
            字段名=model.类型（选项）
            字段名其实就是数据表的属性
            字段名不要使用python，mysql关键字,不要使用连续的下划线__
        3-2 类型 MYSQL的类型
        3-3 选项，是否有默认值，是否为null
            varchar  ->  CharField必须设置max_length
    4.改变表的名称
        默认表的名称是：子应用名_类名        
        修改表的名字    
"""
# Create your models here.
class BookInfo(models.Model):
    # id
    name = models.CharField(max_length=10, unique=True)
    pub_data=models.DateField(null=True)
    readcount=models.IntegerField(default=0)
    commentcount=models.IntegerField(default=0)
    is_delete=models.BooleanField(default=False)


    class Meta:
        db_table='book_info'    # 修改表的名字
        verbose_name = '书籍管理' # admin站点使用的

    # 重写str方法，以显示书籍名字
    def __str__(self):
        return self.name

class PeopleInfo(models.Model):

    # 定义一个有序字典
    GENDER_CHOICES = (
        (1, 'male'),
        (2, 'female'),
    )
    name = models.CharField(max_length=10, unique=True)
    gender = models.SmallIntegerField(choices=GENDER_CHOICES,default=1)
    description = models.CharField(max_length=200, null=True)
    is_delete=models.BooleanField(default=False)
    # 外键约束：人属于哪本书
    """
    外键的级联操作：删除主表从表一起删除
    主表和从表
      1 对 多
    书籍 对 人物
    
    主表的一个数据删除了怎么办？
    
    """
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

    class Meta:
        db_table='people_info'