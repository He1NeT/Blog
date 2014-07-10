#!/usr/bin/env python
#coding:utf-8
import datetime

from django.conf import settings
from django.http import Http404, HttpResponseRedirect
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from app.cms.models import Category, Article
from app.photos.models import Category as photocate, Photos
from app.feedback.forms import GuestBookForm
from app.danye.models import Category as danye_category

def index(request, template):
    index = True
    article = Article.objects.all()
    article_count = article.count()
    click_count = sum([x.click for x in article])
    

    display = 10
    after_range_num = 5
    befor_range_num = 4

    try:
        page = int(request.GET.get("page", 1))
        if page < 1:
            page = 1
    except ValueError:
        page = 1

    paginator = Paginator(Article.objects.all(), display)
    try:
        items = paginator.page(page)
    except:
        items = paginator.page(1)
        #page range
    if page >= after_range_num:
        page_range = paginator.page_range[page-after_range_num:page + befor_range_num]
    else:
        page_range = paginator.page_range[0:int(page) + befor_range_num]
    
    return render(request, template, locals())

def article_tag(request, template, tag):
    display = 10
    after_range_num = 5
    befor_range_num = 4
    
    categories = Category.objects.all()
    articles = Article.objects.filter(tag__icontains=tag)
    
    is_tag = True
    
    try:
        page = int(request.GET.get("page", 1))
        if page < 1:
            page = 1
    except ValueError:
        page = 1
        
    paginator = Paginator(articles, display)
    try:
        items = paginator.page(page)
    except:
        items = paginator.page(1)
    #page range
    if page >= after_range_num:
        page_range = paginator.page_range[page-after_range_num:page + befor_range_num]
    else:
        page_range = paginator.page_range[0:int(page) + befor_range_num]
    return render(request, template, locals())

def article_total(request, template, year, month):
    article = Article.objects.filter(post_time__year=int(year),post_time__month=int(month),)
    is_total = True
    display = 10
    after_range_num = 5
    befor_range_num = 4

    try:
        page = int(request.GET.get("page", 1))
        if page < 1:
            page = 1
    except ValueError:
        page = 1


    paginator = Paginator(article, display)
    try:
        items = paginator.page(page)
    except:
        items = paginator.page(1)
        #page range
    if page >= after_range_num:
        page_range = paginator.page_range[page-after_range_num:page + befor_range_num]
    else:
        page_range = paginator.page_range[0:int(page) + befor_range_num]
    return render(request, template, locals())

def article_list(request, template, category='all'):
    
    display = 10
    after_range_num = 5
    befor_range_num = 4

    try:
        page = int(request.GET.get("page", 1))
        if page < 1:
            page = 1
    except ValueError:
        page = 1
    

    if category:
        if category == "all":
            ps = Article.objects.all().order_by('-id')
        else:
            category = Category.objects.get(name=category)
            ps = Article.objects.filter(category=category.id)
    else:
        ps = Article.objects.all().order_by('-id')

    paginator = Paginator(ps, display)
    try:
        items = paginator.page(page)
    except:
        items = paginator.page(1)
        #page range
    if page >= after_range_num:
        page_range = paginator.page_range[page-after_range_num:page + befor_range_num]
    else:
        page_range = paginator.page_range[0:int(page) + befor_range_num]
    return render(request, template, locals())

def article_detail(request, template, id):
    article = get_object_or_404(Article, pk=id)
    categories = Category.objects.all()
    article.click += 1
    article.save()
    rnews = Article.objects.all().order_by('?')
    return render(request, template, locals())

def feedback(request, template):
    if request.method == 'POST':
        form = GuestBookForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('feedback.thankyou'))
    else:
        form = GuestBookForm()
    return render(request, template, locals())

def photo_list(request, template, category='all'):
    
    display = 30
    after_range_num = 5
    befor_range_num = 4

    photocateies = photocate.objects.all()

    try:
        page = int(request.GET.get("page", 1))
        if page < 1:
            page = 1
    except ValueError:
        page = 1
    

    if category:
        if category == "all":
            ps = Photos.objects.all().order_by('-id')
        else:
            category = photocate.objects.get(name=category)
            ps = Photos.objects.filter(category=category.id)
    else:
        ps = Photos.objects.all().order_by('-id')

    paginator = Paginator(ps, display)
    try:
        items = paginator.page(page)
    except:
        items = paginator.page(1)
        #page range
    if page >= after_range_num:
        page_range = paginator.page_range[page-after_range_num:page + befor_range_num]
    else:
        page_range = paginator.page_range[0:int(page) + befor_range_num]
    return render(request, template, locals())

