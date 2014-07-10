#!/usr/bin/python
#coding:utf-8


from django.conf import settings
from django.contrib import admin
from app.cms.models import Category, Article, Content
from app.feedback.models import GuestBook, GuestBookAdd

#class GuestBookAddAdmin(admin.TabularInline):
#
#    model = GuestBookAdd
#    
#class GuestBookAdmin(admin.TabularInline):
#
#    inlines = [GuestBookAddAdmin]
#    
#    model = GuestBook


    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'is_active', 'treenode','path', 'direct_link', 'has_keywords', 'has_description','article_count']
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

    def article_count(self,obj):
        article_count = obj.articles.all().count()
        return article_count
    article_count.short_description = '文章数'

class ContentAdmin(admin.TabularInline):
    model = Content
    extra = 1
    max_num = 1

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id',  'is_public',  'user', 'category_path', 'title', 'has_keyword', 'has_summary','is_ontop','is_hot', 'is_recommend', 'post_time']
    inlines = [ContentAdmin,]
    search_fields = ['id', 'title', 'author', 'summary']
    raw_id_fields = ['user',]
    #list_per_page = 200
    actions = ['mark_hot', 'mark_recommend', 'mark_ontop','unmark_hot', 'unmark_recommend', 'unmark_ontop']
    list_filter = ['is_public', 'is_ontop' , 'is_recommend', 'is_hot', 'category']


    def category_path(self, obj):
        path = []
        for p in obj.category.path.split(':'):
            c = Category.objects.get(pk=p)
            path.append(c.name)
        return ('>').join(path)
    category_path.short_description = '分类'
    
    def has_keyword(self, obj):
        img = 'no'
        if obj.keyword:
            img = 'yes'
        return '<img src="/static/admin/img/icon-%s.gif">' % img
    has_keyword.short_description = '关键词'
    has_keyword.allow_tags = True

    def has_summary(self, obj):
        img = 'no'
        if obj.summary:
            img = 'yes'
        return '<img src="/static/admin/img/icon-%s.gif">' % img
    has_summary.short_description = '页面描述'
    has_summary.allow_tags = True

    def mark_hot(self, request, queryset):
        queryset.update(is_hot=True)
    mark_hot.short_description = u"设置成热门"
    def unmark_hot(self, request, queryset):
        queryset.update(is_hot=False)
    unmark_hot.short_description = u"取消热门"
    def mark_recommend(self, request, queryset):
        queryset.update(is_recommend=True)
    mark_recommend.short_description = u"设置成推荐"
    def unmark_recommend(self, request, queryset):
        queryset.update(is_recommend=False)
    unmark_recommend.short_description = u"取消推荐"
    def mark_ontop(self, request, queryset):
        queryset.update(is_ontop=True)
    mark_ontop.short_description = u"设置成置顶"
    def unmark_ontop(self, request, queryset):
        queryset.update(is_ontop=False)
    unmark_ontop.short_description = u"取消置顶"

    class Media:
        js = settings.ADMIN_JS

admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
