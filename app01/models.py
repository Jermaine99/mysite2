from django.db import models

# Create your models here.
# 修改表结构只需要在model中修改类， 再执行migration or migrate命令


class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField()


class Department(models.Model):
    tittle = models.CharField(max_length=16)


"""
class Role(models.Model):
    caption = models.CharField(max_length=16)
"""