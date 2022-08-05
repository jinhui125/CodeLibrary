# -*- coding: UTF-8 -*-
import os


class Command:

    @staticmethod
    def adb_command(command):
        """adb_command()方法
            定义：adb指令
            使用方法：Command.adb_command(command)
            参数含义：command：adb指令的字符串
        """
        os.system(command)

    @staticmethod
    def clear_user_data(package):
        Command.adb_command("adb shell pm clear " + package)

