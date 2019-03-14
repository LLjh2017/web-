from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# Create your views here.
from django.urls import reverse


def login_views(request):
    return HttpResponse('这是index应用中的login访问路径')


def register_views(request):
    return HttpResponse('这是index应用中的register访问路径')

def index_views(request):
    return HttpResponse('这是index应用中的index访问路径')

def temp_views(request):
    #1.通过loader加载模板
    t=loader.get_template('01-temp.html')

    #2.将模板渲染成字符串
    html=t.render()

    #3.将字符串通过HttpResponse响应给客户端
    return HttpResponse(html)


def temp02_views(request):
    #通过render加载并响应模板
    return render(request,'01-temp.html')


def var_views(request):
    str='这是模板中的字符串'
    num=3306
    tup=('西游记','水浒传','三国演义','红楼梦')
    list=['孙悟空','西门庆','曹操','林黛玉']
    dic={
        'BJ':'北京',
        'SZ':'深圳',
        'SH':'上海',
    }
    dog=Animal()
    ret = sayhi()
    return render(request,'02-var.html',locals())

def sayhi():
    return 'hello,this is a function...'

class Animal(object):
    name='王富贵'
    def eat(self):
        return 'eat'+self.name


def static_views(request):
    return render(request,'04-static.html')

def alias01_views(request):
    # 通过a02 以及对应的参数，反向解析成a02的地址
    url=reverse('a02',args=('2015',))
    print("a02的地址为："+url)
    return render(request,'05-alias.html')


def alias02_views(request,year):
    print("年份为：",year)
    # 通过a01反向生成对应的地址
    url=reverse('a01')
    print("a01的地址为："+url)
    return render(request,'06-alias.html')


