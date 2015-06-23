# -*- coding: UTF-8 -*- 
from django.db import models

# Create your models here.

class Department(models.Model):
	dep_name = models.CharField(u'部门',max_length=60,unique=True)
	tel_num = models.CharField(u'部门电话',max_length=30)
	email = models.EmailField(u'部门邮箱',blank=True)

	def __unicode__(self):
		return self.dep_name

class Gdyear(models.Model):
    gd_year = models.CharField(u'归档时间',max_length=10,unique=True)

    def __unicode__(self):
        return self.gd_year

class Dangan(models.Model):
	gd_name = models.CharField(u'档案名称',max_length=60)
	gd_department = models.ForeignKey(Department)
	gd_hetong = models.CharField(u'合同号',max_length=30,blank=True)
	gd_time = models.ForeignKey(Gdyear)
	gd_depict = models.CharField(u'描述',max_length=200,blank=True)

	def __unicode__(self):
		return self.gd_name