from django.shortcuts import render
from .models import *
from fruitday.memberapp.models import *
from fruitday.userinfo.models import *
import logging
from django.http import HttpResponse
import json

# Create your views here.


def add_cart(request):
    # 1.声明一个购物车
    # 2.获取用户id
    # 3.获取添加商品的id
    # 4.获取添加数量
    # 5.查询商品
    # 6.查询用户
    # 7.判断商品是否存在
    # 8.转化数量为整数
    # 9.查看是否添加过购物车
    # 10.if true +1
    # 11.elif false save()
    # 12.return
    new_cart = CartInfo()
    user_id = request.session.get('user_id')
    good_id = request.GET.get('goodid')
    good_count = request.GET.get('gcount')
    good_ = Goods.objects.filter(id=good_id)
    user_ = UserInfo.objects.get(id=user_id)
    if len(good_) > 0:
        new_cart.user = user_
        new_cart.good = good_[0]
    else:
        return render(request, 'cart.html')
    new_cart.ccount = int(good_count)
    try:
        oldgo = CartInfo.objects.filter(good_id=good_id, user_id=user_id)
        if len(oldgo) > 0:
            oldgo[0].ccount = oldgo[0].ccount + int(good_count)
            oldgo[0].save()
        else:
            new_cart.save()
    except BaseException as e:
        logging.warning(e)
    return render(request, 'cart.html')


def cart_info(request):
    user_id = request.session.get('user_id')
    find_goods = CartInfo.objects.filter(user=user_id)
    mycartc = 0
    if user_id:
        for find_good in find_goods:
            mycartc += find_good.ccount
    return render(request, 'cart.html', {'find_goods':find_goods, 'mycartc':mycartc})


def delete_cart(request):
    user_id = request.session.get('user_id')
    cart_id = request.GET.get('cart_id')
    try:
        delcart = CartInfo.objects.filter(user_id=user_id, id=cart_id)
        delcart.delete()
    except BaseException as e:
        logging.warning(e)
    content = {'status':"OK", 'text':'删除成功'}
    return HttpResponse(json.dumps(content))

















