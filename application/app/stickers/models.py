#!/usr/bin/env python
#coding:utf-8


from django.conf import settings
from django.db import models


class Stickers(models.Model):
    stickers = models.TextField("内容", blank=True, null=True)
    post_time = models.DateTimeField("留言时间", auto_now_add=True)
        
    class Meta:
        verbose_name = '便贴'
        verbose_name_plural = '便贴管理'

