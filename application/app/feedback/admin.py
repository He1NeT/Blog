#!/usr/bin/env python
#coding:utf-8

from django.conf import settings
from django.contrib import admin
from app.feedback.models import GuestBook, GuestBookAdd

class GuestBookAddAdmin(admin.TabularInline):
    model = GuestBookAdd
    
class GuestBookAdmin(admin.ModelAdmin):
    list_display = ['id','name','qq','post_time']
    inlines = [GuestBookAddAdmin]

admin.site.register(GuestBook, GuestBookAdmin)
