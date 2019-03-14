from django.db.models import Avg, Sum, Count, Q
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

# Create your views here.


def addbook_views(request):
    # Entry.objects.create()
    # 往Book类添加书名
    # book=Book.objects.create(title="小宝宝",publicate_date='2012-08-12')
    # Book.objects.create(title="西游记", publicate_date='2016-10-12')
    # Book.objects.create(title="红楼梦", publicate_date='2017-06-12')
    # Book.objects.create(title="三国演义", publicate_date='2010-10-12')
    # Book.objects.create(title="水浒城", publicate_date='2008-12-12')
    # print('书名的id:'+book.id)
    # book=Book(title="Python")
    # book.publicate_date='2018-10-12'
    # book.save()
    # print('书名的id:' + book.id)
    return HttpResponse('Add Book Success')


def query_views(request):
    # 1.基本查询操作 - all()
    # books = Book.objects.all()
    # print(type(books))
    # print(books)
    # for book in books:
    #     print('ID:%d,书名：%s,出版日期：%s'%(
    #         book.id,book.title,book.publicate_date))
    #     print(books.query)

    # 2.查询返回部分列 values()
    # books = Book.objects.values('title','publicate_date')
    # print(books)
    # for book in books:
    #     print("书名：%s,出版日期：%s"%(book['title'],book['publicate_date']))
    # books = Book.objects.values_list('title','publicate_date')
    # print(books)
    # print(type(books))


    # 3.查询只返回一条数据 - get()
    # book = Book.objects.get(id=8)
    # print(book.title)
    # 1.查询id为8的book的信息
    # list = Book.objects.filter(id=8)
    # print(list)
    # 2.查询Publicate_date为2015-10-12的book的信息
    # list = Book.objects.filter(publicate_date='2015-10-12')
    # print(list)
    # list = Book.objects.filter(id=8,publicate_date = '2015-10-12')
    # print(list)
    # 7.查询年份是18年的
    # list = Book.objects.filter(publicate_date__year=2018)
    # for book in list:
    #     print('ID:%d,书名：%s,出版日期：%s' %
    #           (book.id,book.title,book.publicate_date))
    # list = Book.objects.filter(publicate_date__year__gte=2015)
    # for book in list:
    #     print('ID:%d,书名：%s,出版日期：%s' %
    #           (book.id, book.title, book.publicate_date))

    # 1.查询Author表中age大于等于30的Author的信息
    # list=Author.objects.filter(age__gte=30)
    # for author in list:
    #     print(author.name,author.email,author.age)

    # 2.查询Author表所有姓'王'的Author的信息
    # list=Author.objects.filter(name__startswith= '王')
    # for author in list:
    #     print(author.name)

    # 3.查询Author表中Email中包含'wang'的Author的信息
    # list=Author.objects.filter(email__contains='wang')
    # for author in list:
    #     print(author.name,author.email)

    # 4.查询Author表中age大于'王魏超'的age的Author的信息
    # list=Author.objects.filter(age__gt=Author.objects.get(name='王魏超').age)
    # for author in list:
    #     print(author.name)

    # 查询Author表中age不大于35的Author的信息
    # list=Author.objects.exclude(age__gt=35)
    # for author in list:
    #     print(author.name)

    # 查询按年龄升序排序
    # list=Author.objects.order_by('age')
    # for author in list:
    #     print(author.name,author.age)

    # 查询按年龄降序排序
    # list = Author.objects.order_by('-age')
    # for author in list:
    #     print(author.name, author.age)

    # 查询Author表中所有人的平均年龄 - 聚合函数
    # result=Author.objects.aggregate(avg=Avg('age'))
    # print(result)
    # print('平均年龄为：%d'%result['avg'])

    # 查询Author表中所有人的总年龄 - 聚合函数
    # result = Author.objects.aggregate(avg=Sum('age'))
    # print(result)
    # print('总年龄为：%d' % result['avg'])

    # 查询Book表中每个publicate_date所发行的数量
    # result=Book.objects.values('publicate_date').annotate(
    #     count=Count('title')).values('count','publicate_date').all()
    # print(result)

    # list=Book.objects.filter(id__gt=9).values('publicate_date'
    #                 ).annotate(count=Count('title')).values(
    #     'publicate_date','count').all()
    # print(list)
    # for book in list:
    #     print(book['publicate_date'])
    list = Book.objects.filter(id__gt=9).values('publicate_date'
           ).annotate(count=Count('title')).filter(count__gt=3
           ).values('publicate_date', 'count').all()
    print(list)


    return HttpResponse("<script>alert('查询成功')</script>")


def addauthor_views(request):
    Author.objects.create(name='王魏超',age='35',email='wangwc@163.com')
    Author.objects.create(name='王xiao超', age='25', email='wanwwwwc@163.com')
    Author.objects.create(name='魏超', age='40', email='wangwc@163.com')
    Author.objects.create(name='李魏超', age='30', email='liwangwc@163.com')

    return HttpResponse("<script>alert('插入成功')</script>")

def author_views(request):

    list=Author.objects.filter(isActive=True)


    return render(request,'01-authors.html',locals())

def update_views(request):
    # author=Author.objects.get(id=1)
    # author.age=99
    # author.save()

    # id不等于1
    # authors=Author.objects.exclude(id=1)
    # authors.update(age=55)


    return HttpResponse('Update Success')

def delete_views(request,id):
    # author=Author.objects.get(id=id)
    # author.isActive=False
    # author.save()


    list=Author.objects.filter(id=id)
    list.update(isActive=False)

    return redirect('/04-author')


def doQ_views(request):
    # 获取 id=1 或者 isActive=True 的Author们的信息
    authors = Author.objects.filter(Q(id=1)|Q(isActive=True))
    for au in authors:
        print("ID:%d,Name:%s"%(au.id,au.name))
    return HttpResponse("<script>alert('查询成功')</script>")


def oto_views(request):
    # 声明 wife 对象 并指定其author信息
    # wife = Wife()
    # wife.name = '魏超夫人'
    # wife.age = 30
    # wife.author_id = 1
    # wife.save()


    # wife = Wife()
    # wife.name = '周芷若'
    # wife.age = 19
    # author = Author.objects.get(id=2)
    # wife.author = author
    # wife.save()


    # 查询  正向查询  通过wife查找author
    # wife = Wife.objects.get(id=1)
    # author = wife.author

    # 查询  反向查询  通过author查找wife
    author = Author.objects.get(id=1)
    wife = author.wife

    print("Wife:%s,Author:%s"%(wife.name,author.name))


    return HttpResponse('oto OK')


def otm_views(request):
    # 正向查询 通过Book 查询 Publisher
    book = Book.objects.get(id=1)
    publisher = book.publisher
    print('书籍名称:'+book.title)
    print('所在出版社:'+publisher.name)

    # 反向查询 通过Publisher 查询 Book
    pub = Publisher.objects.get(id=1)
    books = pub.book_set.all()
    print('出版社名称:' + pub.name)
    print("所出版的图书:")
    for book in books:
        print('书籍名称:'+book.title)

    return HttpResponse("Query OK")


def mtm_views(request):
    # 查询id为1的书籍的作者
    book = Book.objects.get(id=1)
    authors = book.author_set.all()
    print('书籍名称:' + book.title)
    for au in authors:
        print("作者:"+au.name)

    # 查询Rapwang所出版的书籍
    author = Author.objects.get(name='Rapwang')
    books = author.book_set.all()
    for book in books:
        print('书籍名称:'+book.title)

    return HttpResponse("Query OK")