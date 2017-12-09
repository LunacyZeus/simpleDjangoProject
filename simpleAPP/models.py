# -*- coding: utf-8 -*-

from django.db import models
from django.utils import timezone
import time,hashlib


# Create your models here.
from django.utils.timezone import now, timedelta

class Test(models.Model):#测试数据表
    Char字段 = models.CharField(verbose_name="Char字段", max_length=32)  # Char字段
    选择 = (('xz1', '选择1'), ('xz2', '选择2'), ('Unkown', '未知'),)
    选择字段 = models.CharField(choices=选择, default='Unkown', verbose_name="选择字段", null=True, max_length=6,blank=True)  # 选择字段
    Decimal字段 = models.DecimalField(verbose_name="Decimal字段", max_digits=16, decimal_places=2, default=0)  # Decimal字段
    布尔字段 = models.BooleanField(verbose_name="布尔字段", default=False, blank=True)  # 布尔字段
    时间字段 = models.DateTimeField(verbose_name='时间字段', blank=True, auto_now_add=True)  # 时间字段
    整数字段 = models.IntegerField(verbose_name="整数字段", default=0, blank=True)  # 整数字段

    #外键 = models.ForeignKey('外键', verbose_name='外键', blank=True, null=True,related_name="merchantUser")  # 外键
    class Meta:
        verbose_name = "测试数据"
        verbose_name_plural = "测试数据"
        ordering = ['-时间字段']


