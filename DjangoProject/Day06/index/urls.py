from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^01-request/$',request_views),

    url(r'^02-referer/$',referer_views),

    url(r'^03-login/$',login_views,name='login'),

    url(r'^04-form/$',form_views),

    url(r'^05-modelform/$',modelform_views),
]