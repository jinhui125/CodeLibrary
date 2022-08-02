# -*- coding: UTF-8 -*-
from enum import Enum


class StartPageElement(Enum):

    # 同意并继续
    Agree_continue_button = 'new UiSelector().resourceId("com.jm.android.jumei:id/commit")'
    # 不同意退出
    Not_agree_exit_button = 'new UiSelector().resourceId("com.jm.android.jumei:id/cancel")'
    # 允许权限
    Allow_permission_button = 'new UiSelector().resourceId("com.android.packageinstaller:id/permission_allow_button")'
    # 拒绝权限
    Reject_permission_button = 'new UiSelector().resourceId("com.android.packageinstaller:id/permission_deny_button")'
