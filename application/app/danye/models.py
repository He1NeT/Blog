#!/usr/bin/python
#coding:utf-8


from django.conf import settings
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import permalink
from django.db.models.signals import pre_save
from django.utils.safestring import mark_safe
from django.template.defaultfilters import striptags

from lib.db.manager import  get_filter_manager


class Category(models.Model):
    name = models.CharField("类别名称", max_length=50)    
    title  = models.CharField("标题", max_length=255, blank=True, null=True)
    parent = models.ForeignKey('self', verbose_name='上一级', null=True, blank=True, related_name='children')
    path = models.CharField("路径", max_length=255, null=True, blank=True, help_text="此项不用填写")
    subtitle = models.CharField("副标题", max_length=255, blank=True, null=True)
    gallery = models.ImageField("图片", upload_to = settings.UPLOAD_TO, blank=True, null=True,)
    author = models.CharField("作者", max_length=255, blank=True, null=True)
    froms = models.CharField("来源", max_length=255, blank=True, null=True)
    is_public = models.BooleanField("是否公开", default=True)
    keywords = models.CharField("页面关键词", max_length=255, null=True, blank=True)
    description = models.CharField("页面描述", blank=True, null=True, max_length=255)
    direct_link = models.CharField("转向链接", max_length=255, null=True, blank=True)
    is_active = models.BooleanField("是否生效", default=True)
    click = models.IntegerField("浏览数", max_length=10, default=1, help_text="此项不用填写")
    post_time = models.DateTimeField("发布时间", auto_now_add=True)
    admin_objects = models.Manager()
    objects = get_filter_manager(is_active=True)

    def __unicode__(self):
        if not self.path:
            return self.name
        if self.id == self.path:
            return self.name
        else:
            return self.node

    def _node(self):
        indent_num = len(self.path.split(':')) -1
        indent = '____' * indent_num
        node = u'%s%s' % (indent, self.name)
        return node
    node = property(_node)
    
    def htmlpath(self):
        paths = []
        for p in self.path.split(':'):
            c = Category.objects.get(pk=p)
            url = c.direct_link or reverse('cms.article.list', kwargs={'id':c.id})
            paths.append('<a href="%s" target="_blank">%s</a>' % (url, c.name))
        return mark_safe("&nbsp; &raquo;&nbsp; ".join(paths))
    
    def _content_counter(self):
        return self.contents.all().count()
    
    @property
    def page_range(self):        
        return range(1, self._content_counter()+1)
        
    
    def get_content(self, n):
        contents = self.contents
        content_counter = contents.all().count()
        if n < 1 or n > content_counter:
            n = 1
        #return contents.all()[n].content
        return contents.all()
    
    #@permalink
    def url(self):
        if len(self.direct_link) > 0:
            return self.direct_link.replace(".","/")
        return ('cms.article.list', '', {'id':self.id})

        
    def get_title(self):
        return self.subtitle or self.title

    def get_gallery(self):
        if self.gallery:
            return self.gallery.thumb_url
        else:
            return '%s%s' % (settings.MEDIA_URL, 'images/no_pic.png')
    
    @property
    def has_children(self):        
        return self.children.all().count() > 0 and True or False
    
    def get_parents(self):
        parents_path = self.path.split(":")
        if len(parents_path)> 1:
            path = parents_path[:-1]
        else:
            path = parents_path
        parents = Category.objects.filter(pk__in=parents_path)
        return parents

    def save(self, * args, ** kwargs):
        super(Category, self).save(*args, ** kwargs)
        if self.parent:
            self.path = '%s:%s' % (self.parent.path, self.id)
        else:
            self.path = self.id
        childrens = self.children.all()
        if len(childrens) > 0:
            for children in childrens:
                children.path = '%s:%s' % (self.path, children.id)
                children.save()
        super(Category, self).save(*args, ** kwargs)
    
    class Meta:
        ordering = ['path']
        verbose_name = '单页'
        verbose_name_plural = '单页管理'

def inital_category_path(sender, instance,** kwargs):
    if instance.id:
        if instance.parent:
            instance.path = '%s:%s' % (instance.parent.path, instance.id)
        else:
            instance.path = instance.id
pre_save.connect(inital_category_path, sender=Category)


class Content(models.Model):
    article = models.ForeignKey(Category, related_name='contents')
    content = models.TextField("内容", blank=True, null=True)

    class Meta:
        ordering = ['id']

    def __unicode__(self):
        return self.content
