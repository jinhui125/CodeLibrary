# -*- coding: UTF-8 -*-
from enum import Enum


class MyPageElement(Enum):

    # 注册/登录
    Registration_or_login_button = 'new UiSelector().text("注册/登录").resourceId(' \
                                   '"com.jm.android.jumei:id/mine_top_register_login_tv") '
    # 会员中心
    Member_entry_button = 'new UiSelector().resourceId("com.jm.android.jumei:id/iv_member_entry")'
