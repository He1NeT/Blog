#!/usr/bin/env python
#coding:utf-8

from django import forms
from captcha.fields import CaptchaField
from app.feedback.models import GuestBook, GuestBookAdd

class GuestBookForm(forms.ModelForm):
    pass
                                        
    class Meta:
        model = GuestBook
        fields = [ 'name', 'qq','email','content']
        
class GuestBookAddForm(forms.ModelForm):
    pass
                                        
    class Meta:
        model = GuestBookAdd
        fields = [ 'name','content']
