from django.conf.urls import url
from .views import *

urlpatterns=[
    # 当访问路径为 index/ 的时候，则将请求交给
    # index_views 视图处理函数取处理
    # 完整的请求路径为 http://localhost:8000/music/index
    # url(r'^index/$',index_views),

    # 当访问路径为 的时候，则将请求交给index_views去处理
    url(r'^$',index_views),
]