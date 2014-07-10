#!/usr/bin/env python
#coding:utf-8

from django import forms
from captcha.fields import CaptchaField
from app.stickers.models import Stickers

class StickersForm(forms.ModelForm):
    pass
                                        
    class Meta:
        model = Stickers
        fields = [ 'stickers']
        

