from django.conf.urls import url
from .views import *

urlpatterns=[
    url(r'^01-addBook/$',addbook_views),

    url(r'^02-query/$',query_views),

    url(r'^03-addAuthor/$',addauthor_views),

    url(r'^04-author/$',author_views),

    url(r'^04-update/$',update_views),

    url(r'^05-delete/(\d+)/$',delete_views),

    url(r'^06-doQ/$',doQ_views),

    url(r'^07-oto/$',oto_views),

    url(r'^08-otm/$',otm_views),

    url(r'^09-mtm/$',mtm_views),
]