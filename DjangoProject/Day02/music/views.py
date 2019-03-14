from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index_views(request):
    return HttpResponse("这是music应用中的index访问路径")
