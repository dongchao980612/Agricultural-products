#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# Time    : 2025/5/17 21:38
# File    : form.py
# Software: PyCharm
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
from django import forms
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        max_length=150,
        # validators=[RegexValidator(r'^[wu4e00-u9fa5.@+-]+$', message='用户名可包含中文、字母、数字和@/./+/-/_')],
        help_text='用户名可包含中文、字母、数字和@/./+/-/_'
    )

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
