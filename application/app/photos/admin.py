#!/usr/bin/env python
#coding: utf-8

from django.conf import settings
from django.contrib import admin
from app.photos.models import Category, Photos

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','path','treenode','images_count',]
    
    
    def path(self, obj):
        if obj.parent:
            return u'%s > %s' % (obj.parent, obj.name)
        return obj.name
    path.short_description = 'path'
    path.allow_tags = True
    
    def treenode(self, obj):
        indent_num = len(obj.path.split(':')) -1
        p = '<div style="text-indent:%spx;">%s</div>' % (indent_num*25, obj.name)
        return p
    treenode.short_description = '路径'
    treenode.allow_tags = True

    def images_count(self,obj):
        count = obj.photos.all().count()
        return count
    images_count.short_description = '项目数'
    
    

class PhotosAdmin(admin.ModelAdmin):
    list_display = ['id', 'is_public', 'name',  'pic','orders', 'post_time']
    list_filter = ['is_public']
    ordering = ['-orders','-id']
    
    def pic(self, obj):
        return '<img src="%s%s" width="80"/ >' % (settings.MEDIA_URL, obj.gallery)
    pic.short_description = '预览图'
    pic.allow_tags = True

admin.site.register(Category, CategoryAdmin)
admin.site.register(Photos, PhotosAdmin)

