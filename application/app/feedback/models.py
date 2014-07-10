#!/usr/bin/env python
#coding:utf-8


from django.conf import settings
from django.db import models
from app.cms.models import Article

class GuestBook(models.Model):
    guestbook = models.ForeignKey(Article, verbose_name="文章留言", related_name="articleguestbook", blank=True, null=True)
    name = models.CharField("昵称", max_length=255, blank=True, null=True)
    qq = models.IntegerField("QQ", max_length=13, blank=True, null=True)
    email = models.EmailField("邮箱",max_length=255, blank=True, null=True)
    content = models.TextField("内容", blank=True, null=True)
    post_time = models.DateTimeField("留言时间", auto_now_add=True)
    
    def __unicode__(self):
        return self.guestbook.title
        
    class Meta:
        verbose_name = '留言'
        verbose_name_plural = '博客留言'
        
class GuestBookAdd(models.Model):
    guestbook = models.ForeignKey(GuestBook, verbose_name="回复留言", related_name="guestbookadd")
    name = models.CharField("昵称", max_length=255, blank=True, null=True)
    content = models.TextField("内容", blank=True, null=True)
    post_time = models.DateTimeField("留言时间", auto_now_add=True)
    
    def __unicode__(self):
        return self.guestbook.name
        
    class Meta:
        verbose_name = '回复留言'
        verbose_name_plural = '博主留言'
