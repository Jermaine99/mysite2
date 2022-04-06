from django.shortcuts import render, HttpResponse, redirect
import requests
from app01 import models

# Create your views here.


def index(requset):
    return HttpResponse('欢迎主页')


def user_list(request):
    return render(request, 'user_list.html')


def vueTest(request):
    name = "world"
    ages = [18, 19, 20]
    user_info = {'name':'xiaoba', 'age': 19}
    return render(request, 'vueTest.html',{'name': name, 'age':ages,'user_info':user_info})


def news(request):
    #去联通 网站抓取数据
    # 向http://www.chinaunicom.com/api/article/NewsByIndex/3/2022/03/news发送请求
    url = 'http://www.chinaunicom.com/api/article/NewsByIndex/3/2022/03/news'
    res = requests.get(url)
    data_list = res.json()

    print(data_list)
    return render(request,'news.html')


def login(request):
    # 登录
    if request.method == "GET":
        return render(request, 'login.html')
    # 如果是POST请求读取用户名和密码
    userName = request.POST.get('user')
    password = request.POST.get('password')

    result = models.UserInfo.objects.filter(name=userName, password=password)

    if result:
        #return HttpResponse("登录成功")
        # 跳转外部链接
        #return redirect('/user/list/')
        print(request)
        return redirect('/user/list')

    return render(request, 'login.html', {"error_meg":"用户名或密码错误"})


def orm(request):
    ## 添加表
    """
    models.Department.objects.create(tittle="销售部")
    models.Department.objects.create(tittle="IT部门")
    models.Department.objects.create(tittle="运营部门")
    """

    # models.Department.objects.filter(id=3).delete() # 删除ID为3
    # models.Department.objects.all().delete()    # 删除所有

    # 获取数据 对象
    """
    data_list = models.Department.objects.all()
    print(data_list)    # <QuerySet [<Department: Department object (7)>
    for obj in data_list:
        print(obj.id)
        print(obj.tittle)
    """

    # 更新对象
    # models.Department.objects.filter(id=7).update(tittle = "xiaoshou")
    models.UserInfo.objects.create(name="Java", password="991", age=12)
    models.UserInfo.objects.create(name="C++", password="181", age=18)
    models.UserInfo.objects.create(name="Python", password="178", age=22)
    return HttpResponse("成功")


def user_info(request):

    data = models.UserInfo.objects.all()
    return render(request, 'user_info.html', {"data": data})


def resign(request):
    # 注册添加用户
    print(request)
    if request.method == "GET":
        return render(request, 'resign.html')

    userName = request.POST.get('user')
    password = request.POST.get('password')
    age = request.POST.get('age')
    models.UserInfo.objects.create(name=userName, password=password, age=age)
    result = models.UserInfo.objects.filter(name=userName, password=password)
    if result:
        return redirect('/login')
    else:
        return HttpResponse("注册失败")


def delete(request):

    nid = request.GET.get("nid")
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/user/list')