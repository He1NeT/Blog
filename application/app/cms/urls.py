#!/usr/bin/env python
#coding:utf-8

from django.conf.urls import include, url, patterns

urlpatterns = patterns('app.cms.views',
    url(r'^(?P<id>\d+)/$', 'article_detail', {'template':'cms/article/detail.html'}, name='cms.article.detail'),
    url(r'^cate/(?P<cid>\d+)/$', 'article_list', {'template':'cms/article/list.html'}, name='cms.article.list'),
    url(r'detail/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/(?P<id>\d+)/',
        'article_detail',
        {'template':'cms/article/detail.html'},
        name='cms.article.ymdetail'),                   
    )
