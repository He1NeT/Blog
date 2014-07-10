#!/usr/bin/env python
#coding:utf-8

from django.conf import settings
from django.contrib import admin
from app.stickers.models import Stickers


class StickersAdmin(admin.ModelAdmin):
    list_display = ['id','stickers']


admin.site.register(Stickers, StickersAdmin)
