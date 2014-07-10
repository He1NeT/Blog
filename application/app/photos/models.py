#!/usr/bin/env python
#coding: utf-8

from django.conf import settings
from django.db import models
from lib.db.manager import get_filter_manager

class Category(models.Model):
    name = models.CharField("照片分类", max_length=255)
    parent = models.ForeignKey('self', verbose_name='上一级', null=True, blank=True, related_name='children')
    
    def __unicode__(self):
        return self.name

    def _node(self):
        indent_num = len(self.path.split(':')) -1
        indent = '____' * indent_num
        node = u'%s%s' % (indent, self.name)
        return node
    node = property(_node)
    
    def url(self):
        return self.get_absolute_url()

    @models.permalink
    def get_absolute_url(self):
        return ('photos.list', None, {'category':self.name})

    class Meta:
        ordering = ['id']
        verbose_name = '相片分类'
        verbose_name_plural = '相片分类管理'

class Photos(models.Model):
    category = models.ForeignKey(Category, verbose_name="相片分类", related_name='products')
    name = models.CharField("相片标题", max_length=255, blank=True, null=True)
    small_gallery = models.ImageField(upload_to=settings.UPLOAD_TO, verbose_name="相片小图", blank=True, null=True)
    gallery = models.ImageField(upload_to=settings.UPLOAD_TO, verbose_name="相片图片")
    desc = models.TextField(verbose_name="相片描述", blank=True, null=True)
    orders = models.IntegerField(verbose_name="排序", default=1, help_text="数字越大越靠前")
    is_public = models.BooleanField(default=True, verbose_name="是否公开")
    post_time = models.DateTimeField(auto_now_add=True)
    admin_objects = models.Manager()
    objects = get_filter_manager(is_public=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['-orders','-id']
        verbose_name = '相片'
        verbose_name_plural = '相片管理'
