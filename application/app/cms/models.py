#!/usr/bin/python
#coding:utf-8

from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.sites.managers import CurrentSiteManager
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import permalink
from django.db.models.signals import pre_save
from django.utils.safestring import mark_safe
from django.template.defaultfilters import striptags

from lib.db.manager import  get_filter_manager


class Category(models.Model):
    name = models.CharField("类别名称", max_length=50)    
    parent = models.ForeignKey('self', verbose_name='上一级', null=True, blank=True, related_name='children')
    path = models.CharField("路径", max_length=255, null=True, blank=True, help_text="此项不用填写")
    keywords = models.CharField("页面关键词", max_length=255, null=True, blank=True)
    description = models.TextField("页面描述", blank=True, null=True)
    direct_link = models.CharField("转向链接", max_length=255, null=True, blank=True)
    orders = models.IntegerField(verbose_name="排序", default=1, help_text="数字越大越靠前")
    is_active = models.BooleanField("是否生效", default=True)
    #sites   = models.ManyToManyField(Site, verbose_name='站点', related_name='article_categories')
    admin_objects = models.Manager()
    #objects = get_filter_manager(is_active=True)
    objects = models.Manager()
    #on_site = CurrentSiteManager()

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
    
    
    #@permalink
    def url(self):
        if len(self.direct_link) > 0:
            return '%s' % self.direct_link.replace(".","/")
        return ('cms.article.list',  None,  {'id':self.id})
    
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
        verbose_name = '分类'
        verbose_name_plural = '文章分类'

def inital_category_path(sender, instance,** kwargs):
    if instance.id:
        if instance.parent:
            instance.path = '%s:%s' % (instance.parent.path, instance.id)
        else:
            instance.path = instance.id
pre_save.connect(inital_category_path, sender=Category)

class Article(models.Model):
    user = models.ForeignKey(User, verbose_name='用户', default=1, on_delete=models.SET_NULL, blank=True, null=True)
    category = models.ForeignKey(Category, verbose_name='分类', related_name='articles', 
                                 on_delete=models.SET_NULL, blank=True, null=True)
    is_ontop = models.BooleanField("是否置顶", default=False)
    title  = models.CharField("标题", max_length=255)
    subtitle = models.CharField("副标题", max_length=255, blank=True, null=True)
    remark = models.CharField("备注", max_length=255, blank=True, null=True)
    direct_link = models.CharField("转向链接", max_length=255, blank=True, null=True)
    gallery = models.ImageField("图片", upload_to = settings.UPLOAD_TO, blank=True, null=True,)
    author = models.CharField("作者", max_length=255, blank=True, null=True)
    froms = models.CharField("来源", max_length=255, blank=True, null=True)
    tag = models.CharField("标签", max_length=255, blank=True, null=True)
    keyword = models.CharField("页面关键词", max_length=255, blank=True, null=True)
    summary = models.TextField("内容简介", blank=True, null=True)
    click = models.IntegerField("浏览数", max_length=10, default=1, help_text="此项不用填写")
    is_hot  = models.BooleanField("是否热门", default=False)
    is_recommend = models.BooleanField("是否推荐", default=False)
    is_public = models.BooleanField("是否公开", default=True)
    enable_comment = models.BooleanField("是否允许评论", default=True)
    post_time = models.DateTimeField("发布时间", auto_now_add=True)
    modify_time  = models.DateTimeField(auto_now_add=True, auto_now=True)
    #manager
    admin_objects = models.Manager()
    objects = get_filter_manager(is_public=True)
    #sites   = models.ManyToManyField(Site, related_name='content_articles')
    #on_site = CurrentSiteManager()
    hot = get_filter_manager(is_hot=True)
    recommend = get_filter_manager(is_recommend=True)

    def __unicode__(self):
        return self.subtitle or self.title

    def get_title(self):
        return self.subtitle or self.title
    
    @property
    def get_month(self):
        return self.post_time.month
    
    @property
    def get_year(self):
        return self.post_time.year
    
    @property
    def get_tag(self):
        if self.tag != None:
            return [i for i in self.tag.split(',') if len(i)>0]
        return None
    
    def get_gallery(self):
        if self.gallery:
            return self.gallery.thumb_url
        else:
            return '%s%s' % (settings.MEDIA_URL, 'images/no_pic.png')

    def get_keyword_html(self):
        if self.keyword:
            keywords = self.keyword.split(' ')
            keywords_html_list = ['<li><a href="/content/tag/%s/" target=_blank>%s</a></li>' % (k, k) for k in keywords if k]
            return ('').join(keywords_html_list)
    
    def get_summary(self):
        summary =  ''
        if len(self.summary):
            summary = self.summary
        else:
            contents = self.contents.all()
            if len(contents) > 0:
                summary = contents[0].content
                summary = striptags(mark_safe(summary))
                summary = summary.replace('&nbsp;', '')
                summary = summary.replace('&rdquo;','')
                summary = summary.replace('&ldquo;','')
                summary = summary.replace('\r','')
                summary = summary.replace('\n','')
        return striptags(summary)
    
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
    
    @permalink
    def ymdurl(self):
        if self.direct_link:
            return self.direct_link
        else:
            return ('cms.article.ymddetail', 
                    None, 
                    {'id':self.id,
                     'year': self.post_time.year,
                     'month':self.post_time.month,
                     'day':self.post_time.day,})
    
    @permalink
    def url(self):
        if self.direct_link:
            return self.direct_link
        else:
            return ('cms.article.detail',  None,  {'id':self.id})
            
    class Meta:
        ordering = ['-is_ontop','-id']
        verbose_name = '文章'
        verbose_name_plural = '文章管理'
        

class Content(models.Model):
    article = models.ForeignKey(Article, related_name='contents')
    content = models.TextField("内容", blank=True, null=True)

    class Meta:
        ordering = ['id']

    def __unicode__(self):
        return self.content
