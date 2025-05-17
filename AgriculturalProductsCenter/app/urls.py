#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# Time    : 2025/5/17 19:52
# File    : urls.py
# Software: PyCharm
from django.contrib.auth.views import LogoutView
from django.urls import path


from .views import *

urlpatterns = [

    # 用户认证
    path('register/', user_register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', LogoutView.as_view(next_page='/login/', http_method_names=['get', 'post']),
         name='logout'),

    # 个人中心
    path('profile/', user_profile, name='profile'),


    # 商品
    path('products/', product_list, name='products'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
    ]