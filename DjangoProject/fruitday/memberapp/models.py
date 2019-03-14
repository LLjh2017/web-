from django.db import models

# Create your models here.
class GoodsType(models.Model):
    title = models.CharField('名称', max_length=30)
    desc = models.CharField('描述', max_length=200, default='商品描述')
    picture = models.ImageField('图片', upload_to='static/img/good_type', default='normal.png')
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'goods_type'

class Goods(models.Model):
    title = models.CharField('名称', max_length=50)
    price = models.DecimalField('商品价格', max_digits=8, decimal_places=2)
    unit = models.CharField('单位', max_length=20, default='500g')
    desc = models.CharField('描述', max_length=1000)
    detail = models.CharField('商品详情', max_length=2000, default='商品详情')
    picture = models.ImageField('商品照片', upload_to='static/images/goods', default='normal.png')
    isDelete = models.BooleanField(default=False)
    type = models.ForeignKey(GoodsType)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/detail/?good={}'.format(self.id)

    class Meta:
        db_table = 'goods'