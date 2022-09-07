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
    # 首页-标题栏
    Front_title_button = 'new UiSelector().text("首页").resourceId("com.jm.android.jumei:id/text")'
    # 极速免税店-标题栏
    Duty_free_shop_button = 'new UiSelector().text("极速免税店").resourceId("com.jm.android.jumei:id/text")'
    # 旗舰店-标题栏
    Flagship_store = 'new UiSelector().text("旗舰店").resourceId("com.jm.android.jumei:id/text")'
    # 母婴-标题栏
    Mother_baby = 'new UiSelector().text("母婴").resourceId("com.jm.android.jumei:id/text")'
    # 首页-搜索栏
    search_bar = 'new UiSelector().resourceId("com.jm.android.jumei:id/tv_go_search")'
    # 搜索-输入栏
    search_input = 'new UiSelector().resourceId("com.jm.android.jumei:id/search_input")'
    # 热榜推荐
    Hot_list_recommendation = 'new UiSelector().resourceId("com.jm.android.jumei:id/iv_hot_list_title")'
    # 感兴趣热度
    Interest = 'new UiSelector().textContains("人感兴趣").resourceId("com.jm.android.jumei:id/tv_description")'
    # 左菜单栏
    Left_menu_button = 'new UiSelector().resourceId("com.jm.android.jumei:id/iv_left_menu")'
    # 左菜单栏选项-扫一扫
    Scan_QR_code_button = 'new UiSelector().text("扫一扫").resourceId("com.jm.android.jumei:id/tv_menu_name")'
    # 左菜单栏选项-宝箱
    Treasure_chest_button = 'new UiSelector().text("宝箱").resourceId("com.jm.android.jumei:id/tv_menu_name")'
    # 左菜单栏选项-消息
    Information_button = 'new UiSelector().text("消息").resourceId("com.jm.android.jumei:id/tv_menu_name")'
    # 左菜单栏选项-意见反馈
    Feedback_button = 'new UiSelector().text("意见反馈").resourceId("com.jm.android.jumei:id/tv_menu_name")'
    # 首页-购物车添加按钮
    Add_cart_button = 'new UiSelector().resourceId("com.jm.android.jumei:id/iv_add_cart")'
    # 商品详情页-购物车添加按钮
    Commodity_confirm_add_button = 'new UiSelector().text("加入购物车").' \
                                   'resourceId("com.jm.android.jumei:id/product_sku_confirm_btn")'
    # 指定商品种类选择按钮
    Commodity_type_selection_button = 'new UiSelector().resourceId("com.jm.android.jumei:id/tv_sku_name")'
    # 指定商品-购买数量-文本
    Commodity_purchase_quantity_text = 'new UiSelector().text("购买数量").' \
                                       'resourceId("com.jm.android.jumei:id/tv_num_group_title")'
    # 指定商品-购买数量输入框
    Commodity_purchase_quantity_input = 'new UiSelector().resourceId("com.jm.android.jumei:id/product_edit_num")'
