from django.http import HttpResponse
from django.shortcuts import render
from .forms import *

# Create your views here.
def request_views(request):
    # print(dir(request))
    print(request.META)

    scheme = request.scheme
    body = request.body
    path = request.path
    host = request.get_host()
    method = request.method
    get = request.GET
    post = request.POST
    cookies = request.COOKIES

    return render(request,'01-request.html',locals())

def referer_views(request):
    #获取请求源地址,如果没有源地址 则获取一个 /
    referer = request.META.get('HTTP_REFERER','/')
    return HttpResponse("Referer is : "+referer)


def login_views(request):
    if request.method == 'GET':
        return render(request,'03-login.html')
    else:
        # 接收前端传递过来的数据 输出在终端上
        uname=request.POST['uname']
        uu=request.POST.get('uname')
        upwd=request.POST['upwd']
        uup=request.POST.get('upwd')
        print(uname,upwd)
        print(uu,uup)
        return HttpResponse("Recived post request successful")

def form_views(request):
    if request.method=='GET':
        form = RemarkForm()
        return render(request,'04-form.html',locals())
    else:
        # 1.通过RemarkForm的构造函数，接收请求提交数据
        form = RemarkForm(request.POST)
        # 2.通过验证
        if form.is_valid():
            # 3.通过验证之后再取值
            cd = form.cleaned_data
            print(cd)
        return HttpResponse("取值成功")

def modelform_views(request):
    if request.method=="GET":
        # 创建RegisterForm的对象，并发送到模板上
        form = RegisterForm()
        return render(request,'05-modelform.html',locals())
    else:
        # 将request.POST传递给RegisterForm的构造函数
        form = RegisterForm(request.POST)
        # 让form通过验证
        if form.is_valid():
            # 取值
            user = User(**form.cleaned_data)
            # 保存到数据库
            # user.save()
            print("uname:%s,upwd:%s,uemai:%s"%(
                user.uname,user.upwd,user.uemail))
        return HttpResponse("取值成功")