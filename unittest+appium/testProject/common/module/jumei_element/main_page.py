# -*- coding: UTF-8 -*-
from enum import Enum


class MainPageElement(Enum):

    # 我的
    My_button = 'new UiSelector().text("我的").resourceId("com.jm.android.jumei:id/tv_tab_name")'
    # 购物车
    Shopping_cart_button = 'new UiSelector().text("购物车").resourceId("com.jm.android.jumei:id/tv_tab_name")'
    # 分类
    Classification_button = 'new UiSelector().text("分类").resourceId("com.jm.android.jumei:id/tv_tab_name")'
    # 首页
    Front_page_button = 'new UiSelector().text("首页").resourceId("com.jm.android.jumei:id/tv_tab_name")'
