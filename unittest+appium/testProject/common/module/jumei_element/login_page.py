# -*- coding: UTF-8 -*-
from enum import Enum


class LoginPageElement(Enum):
    # 手机注册/登录
    Phone_registration_or_login_button = 'new UiSelector().resourceId("com.jm.android.jumei:id/tab_login_phone")'
    # 账号密码登录
    Account_password_login_button = 'new UiSelector().resourceId("com.jm.android.jumei:id/tab_login_account")'
    # 手机号/邮箱/用户名
    Account_input = 'new UiSelector().resourceId("com.jm.android.jumei:id/lg_user_name")'
    # 6-16位密码
    Password_input = 'new UiSelector().resourceId("com.jm.android.jumei:id/lg_password")'
    # 《聚美用户协议》、《聚美隐私权政策》
    Protocol_button = 'new UiSelector().resourceId("com.jm.android.jumei:id/license_select")'
    # 登录
    Login_button = 'new UiSelector().resourceId("com.jm.android.jumei:id/login_account")'
    # 账号密码错误-toast弹框-XPATH
    toast = "//*[@class='android.widget.Toast']"
    # 《聚美用户协议》
    User_agreement_textLink = 'new UiSelector().resourceId("com.jm.android.jumei:id/license_agree")'
    # 《聚美隐私权政策》
    Privacy_textLink = 'new UiSelector().resourceId("com.jm.android.jumei:id/license_privacy_policy")'
    # 聚美用户协议界面标题
    User_agreement_title = 'new UiSelector().text("聚美用户协议").resourceId("com.jm.android.jumei:id/title")'
    # 聚美隐私权政策界面标题
    Privacy_title = 'new UiSelector().text("聚美隐私权政策").resourceId("com.jm.android.jumei:id/title")'
    # 聚美用户协议界面、聚美隐私权政策界面-关闭按钮
    Privacy_agreement_close_button = 'new UiSelector().resourceId("com.jm.android.jumei:id/close_ImgBtn")'
    # 聚美用户协议界面、聚美隐私权政策界面-返回按钮
    Privacy_agreement_back_button = 'new UiSelector().resourceId("com.jm.android.jumei:id/back")'
    # 聚美用户协议界面、聚美隐私权政策界面-刷新按钮
    Privacy_agreement_refresh_button = 'new UiSelector().resourceId("com.jm.android.jumei:id/refresh_ImgBtn")'
    # 聚美用户协议界面、聚美隐私权政策界面-分享按钮
    Privacy_agreement_share_button = 'new UiSelector().resourceId("com.jm.android.jumei:id/share")'
    # 聚美用户协议界面-部分内容
    User_agreement_context = 'new UiSelector().textContains("管理者之间所订立的契约，具有合同的法律效力，请您仔细阅读")'

    # 第三方账号登录
    Third_party_account_title = 'new UiSelector().text("第三方账号登录").resourceId("com.jm.android.jumei:id/login_ext_title")'
    # 微博登录跳转按钮
    Weibo_imageLink = 'new UiSelector().resourceId("com.jm.android.jumei:id/login_ext_layout").' \
                      'childSelector(new UiSelector().resourceId("com.jm.android.jumei:id/ext_login_item_layout").' \
                      'index(0)).childSelector(new UiSelector().resourceId("com.jm.android.jumei:id/ext_login_icon"))'
    # 微博登录界面标题
    Weibo_title = 'new UiSelector().text("微博登录")'
    # 微博登录界面关闭按钮
    Weibo_close_button = 'new UiSelector().text("关闭")'

    # QQ登录跳转按钮
    QQ_imageLink = 'new UiSelector().resourceId("com.jm.android.jumei:id/login_ext_layout").' \
                   'childSelector(new UiSelector().resourceId("com.jm.android.jumei:id/ext_login_item_layout").' \
                   'index(1)).childSelector(new UiSelector().resourceId("com.jm.android.jumei:id/ext_login_icon"))'
    # QQ登录界面下载按钮
    QQ_downLoad_button = 'new UiSelector().text("下载QQ").resourceId("downLoadBtn")'

    # 支付宝登录跳转按钮
    ZhiFuBao_imageLink = 'new UiSelector().resourceId("com.jm.android.jumei:id/login_ext_layout").' \
                         'childSelector(new UiSelector().resourceId("com.jm.android.jumei:id/ext_login_item_layout").' \
                         'index(2)).childSelector(new UiSelector().resourceId("com.jm.android.jumei:id/ext_login_icon"))'
    # 支付宝登录界面标题
    ZhiFuBao_title = 'new UiSelector().text("登录支付宝").className("android.view.View")'
    # 支付宝登录界面返回按钮
    ZhiFuBao_back_button = 'new UiSelector().description("com.android.auth")'
