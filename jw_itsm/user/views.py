from django.shortcuts import render, redirect
from django.http import HttpResponse

# 展示用户登录界面
def login(request):
    return render(request, "login.html")

# 接收用户名，密码，处理
def process(request):
    # 接收用户名、密码
    username = request.POST.get("username")
    password = request.POST.get("password")
    if username == "admin" and password == "123":
        return redirect("/index/")
    else:
        return redirect("/login/")

# 主页
def index(request):
    # 接收登录传递的用户名
    username = request.GET.get("username")
    return render(request, "index.html")