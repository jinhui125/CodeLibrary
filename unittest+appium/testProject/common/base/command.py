# -*- coding: UTF-8 -*-
import os


class Command:

    def adb_command(command):
        """adb_command()方法
            定义：adb指令
            使用方法：Command.adb_command(command)
            参数含义：command：adb指令的字符串
        """
        os.system(command)
