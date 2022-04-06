"""mysite2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import app01.views


urlpatterns = [

    #path('admin/', admin.site.urls),

    path('index/', app01.views.index),
    path('user_list/', app01.views.user_list),
    path('vueTest/', app01.views.vueTest),
    path('news/', app01.views.news),
    path('login/', app01.views.login),
    path('orm/', app01.views.orm),
    path('user/list', app01.views.user_info),
    path('resign/', app01.views.resign),
    path('delete/', app01.views.delete)
]
