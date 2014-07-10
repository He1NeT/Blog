#!/usr/bin/python
#coding:utf-8
#desc: 
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic.simple import redirect_to, direct_to_template
import captcha
from app.cms.models import Category
from app.danye.models import Category as danye_category

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^(static|public)/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
    url(r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '%sfavicon.ico' % settings.MEDIA_URL}),
    url(r'^e4eefb0da89ba277e57a96d1e45b958a\.html$', 'django.views.generic.simple.redirect_to', {'url': '%se4eefb0da89ba277e57a96d1e45b958a.html' % settings.MEDIA_URL}),
    url(r'^captcha/', include('captcha.urls')),
    #url(r'^user/', include('app.user.urls')),
)

#static file
urlpatterns += patterns('',
    url(r'^(static|public)/(?P<path>.*)$',
        'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
            }),
)

urlpatterns += patterns('views',
    url(r'^$',  'index', {'template':'index.html'}, name='index'),
    url(r'^tag/(?P<tag>.*)/$', 'article_tag', {'template':'list.html'}, name='cms.article.tag'),
    url(r'^(?P<year>\d+)/(?P<month>\d+)/','article_total',{'template':'list.html'},name='cms.article.ymdetail'),
    url(r'^(?P<id>\d+)/$',  'article_detail', {'template':'page.html'}, name='cms.article.detail'),
    url(r'^category/(?P<category>.*)/$',  'article_list', {'template':'list.html'}, name='cms.article.list'),
    url(r'^photo/(?P<category>.*)/$',  'photo_list', {'template':'photo.html'}, name='photo.list'),

)


urlpatterns += patterns('',
    #url(r'^feedback/thankyou/$', direct_to_template, {'template':'static/feedback.thankyou.html'}, name='feedback.thankyou'),

)