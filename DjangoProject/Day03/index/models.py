from django.db import models

# Create your models here.


# 1.name:出版社名称 - varchar
# 2.address:出版社地址 - varchar
# 3.city:出版社所在城市 - varchar
# 4.country:出版社所在国家 - varchar
# 5.website:出版社网址 - varchar
class Publisher(models.Model):
    name = models.CharField(max_length=30,verbose_name='出版社')
    address = models.CharField(max_length=200,verbose_name='地址')
    city = models.CharField(max_length=30,verbose_name='城市')
    country = models.CharField(max_length=30,verbose_name='国家')
    website = models.URLField(verbose_name='网站')

    def __str__(self):
        return self.name

    class Meta:
        db_table='Publisher'
        verbose_name='出版社'
        verbose_name_plural = verbose_name






# 在 index 应用中的 models.py 中追加两个 class
#   1.Author - 作者
#     1.name - 姓名
#     2.age  - 年龄
#     3.email- 邮箱(允许为空)
class Author(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField(null=True)
    isActive=models.BooleanField(default=True)

    # 重写 __str__ 函数 以便定义对象在后台的表现名称
    def __str__(self):
        return self.name

    class Meta:
        # 1.指定表名
        db_table='author'
        # 2.指定在 admin 中显示的名称
        verbose_name='作者'
        # 3.指定在 admin 中的显示的名称
        verbose_name_plural=verbose_name
        # 4.指定在 admin 中按照 年龄降序排序
        ordering=['-age']



# 2.Book - 图书
#    1.title - 书名
#    2.Publicate_date - 出版时间
class Book(models.Model):
    title = models.CharField(max_length=50,verbose_name='书名')
    publicate_date = models.DateField(verbose_name='出版时间')

    # 增加对publisher(一)对多的引用关系
    publisher =  models.ForeignKey(Publisher)

    # 增加对Author(多)对多的引用关系
    author_set = models.ManyToManyField(Author)

    def __str__(self):
        return self.name

    class Meta:

        db_table='book'
        verbose_name='书籍'
        verbose_name_plural = verbose_name
        ordering=['-publicate_date']

class Wife(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    # 增加对 Author 的一对一关联关系
    author = models.OneToOneField(Author)

    def __str__(self):
        return self.name
    class Meta:
        db_table='wife'
