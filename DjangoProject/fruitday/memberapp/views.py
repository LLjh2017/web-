from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import *
import random
from django.db import DatabaseError
import logging
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def index(request):
    try:
        good_fruit_type = get_object_or_404(GoodsType, title='新鲜水果')
        fruit_goods = random.sample(list(good_fruit_type.goods_set.all()), 2)
    except DatabaseError as e:
        logging.warning(e)
    return render(request, 'index.html', {'good_list':locals()})


def detail_one(request):
    good_id = request.GET.get('good')
    try:
        goodone = Goods.objects.filter(id=good_id)
    except ObjectDoesNotExist as e:
        logging.warning(e)
    return render(request, 'detail.html', {'goodone':goodone[0]})












