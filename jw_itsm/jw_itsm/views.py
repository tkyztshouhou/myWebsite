from django.http import HttpResponse
from django.shortcuts import render

# 显示hello world
def hello(request):
    return HttpResponse("<h1>Hello world</h1> ")

# 默认主页
def index(request):
    return render(request, 'index.html')

#TemplateDoesNotExist at /../templates/index.html 
