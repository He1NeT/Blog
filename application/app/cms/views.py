#!/usr/bin/python
#coding:utf-8


from django.core.paginator import Paginator, EmptyPage, InvalidPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from app.cms.models import Category, Article

def index(request, template):
    return render(request, template, locals())


def category(request, template):
    return render(request, template, locals())

def article_list(request, template, cid):
    display = 20
    after_range_num = 5
    befor_range_num = 4

    try:
        page = int(request.GET.get("page", 1))
        if page < 1:
            page = 1
    except ValueError:
        page = 1
    
    category = get_object_or_404(Category, pk=cid)
        
    paginator = Paginator(category.articles.all(), display)
    try:
        items = paginator.page(page)
    except(EmptyPage, InvalidPage, PageNotAnInteger):
        items = paginator.page(1)
    #page range
    if page >= after_range_num:
        page_range = paginator.page_range[page-after_range_num:page + befor_range_num]
    else:
        page_range = paginator.page_range[0:int(page) + befor_range_num]
    
    top_clicks = Article.objects.all().order_by('-click')[:10]
    return render(request, template, locals())

def article_detail(request, template, year, month, day, id):
    article = get_object_or_404(Article, pk=id,
                                         post_time__year=year,
                                         post_time__month=month,
                                         post_time__day=day,)
    try:
        page = int(request.GET.get("page", 1))
        if page < 1:
            page = 1            
    except ValueError:
        page = 1
    article.content = article.get_content(page)
    
    return render(request, template, locals())
