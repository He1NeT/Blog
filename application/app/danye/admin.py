#!/usr/bin/python
#coding:utf-8


from django.conf import settings
from django.contrib import admin
from app.danye.models import Category, Content

class ContentAdmin(admin.TabularInline):
    model = Content
    extra = 1
    max_num = 1

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'is_active', 'title', 'treenode','path', 'direct_link', 'has_keywords', 'has_description', 'post_time']
    inlines = [ContentAdmin,]
    search_fields = ['id', 'title', 'author', 'description']
    ordering = ['path']
    list_per_page = 1000
    raw_id_fields = ['parent', ]
    list_filter = ['is_active', ]

    def path(self, obj):
        if obj.parent:
            return u'%s > %s' % (obj.parent, obj.name)
        return obj.name
    path.short_description = 'path'
    path.allow_tags = True

    def has_keywords(self, obj):
        img = 'no'
        if obj.keywords:
            img = 'yes'
        return '<img src="/static/admin/img/icon-%s.gif">' % img
    has_keywords.short_description = '关键词'
    has_keywords.allow_tags = True

    def has_description(self, obj):
        img = 'no'
        if obj.description:
            img = 'yes'
        return '<img src="/static/admin/img/icon-%s.gif">' % img
    has_description.short_description = '页面描述'
    has_description.allow_tags = True

    def treenode(self, obj):
        indent_num = len(obj.path.split(':')) -1
        p = '<div style="text-indent:%spx;">%s</div>' % (indent_num*25, obj.name)
        return p
    treenode.short_description = '路径'
    treenode.allow_tags = True
    
    class Media:
        js = settings.ADMIN_JS



admin.site.register(Category, CategoryAdmin)
