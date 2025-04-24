#!/usr/bin/python
# -*- coding:utf-8 -*-
# @auther    : jinhui
# @dateTime  : 2025-04-24
# @function  : 公共方法类
# @version   : V1.0

import os
import sys
import time
import signal
import datetime
import subprocess

class CommonFunc:

    def __init__(self, signal_flag = False):
        self.signal_flag = signal_flag
    
    def dynamic_string(self, dynamic_string_style, text_description, delay_time = 0.25, bar_time = 0, wait_style = 'circle', bar_style = '▋', count = 1):

        wait_style_dict = {
                                    'circle': ['\\', '|', '/', '-'], 
                                    'columnar': ['▁', '▂', '▃', '▄', '▅', '▆', '▇', '█'],
                                    'poker_suit': ['♠️ ', '♥️ ', '♦️ ', '♣️ '],
                                    'moon': ['🌕', '🌖', '🌗', '🌘', '🌑', '🌒', '🌓', '🌔'],
                                    'clock': ['🕛', '🕐', '🕑', '🕒', '🕓', '🕔', '🕕', '🕖', '🕗', '🕘', '🕙', '🕚'],
                                    'playing_cards': ['🂱', '🂲', '🂳', '🂴', '🂵', '🂶', '🂷', '🂸', '🂹', '🂺', '🂻', '🂼', '🂽', '🂾', '🂡', '🂢', '🂣', '🂤', '🂥', '🂦', '🂧', '🂨', '🂩', '🂪', 
                                                '🂫', '🂬', '🂭', '🂮', '🃁', '🃂', '🃃', '🃄', '🃅', '🃆', '🃇', '🃈', '🃉', '🃊', '🃋', '🃌', '🃍', '🃎', '🃑', '🃒', '🃓', '🃔', '🃕', '🃖', 
                                                '🃗', '🃘', '🃙', '🃚', '🃛', '🃜', '🃝', '🃞', '🃏']

                                }

        if dynamic_string_style == 'proress_bar':
            for i in range(1, 101):
                print(f'\r{text_description}: {bar_style * (i // 2)} 倒计时: {bar_time - (i // (100/bar_time))}s', end='', flush=True)
                time.sleep(bar_time/100)
                
        elif dynamic_string_style == 'wait_animation':
            print(f'\r{text_description} {wait_style_dict[wait_style][count % len(wait_style_dict[wait_style])]}', end='', flush=True)
            time.sleep(delay_time)

        else:
            pass

    def signal_handler(self, sig, frame):

        self.signal_flag = True

    def handle_signal(self, subprocess_obj, text_description, wait_style = 'circle', delay_time = 0.25):

        print(f'开始执行时间: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
        tmp_count = 1

        while not self.signal_flag:

            tmp_count += 1
            self.dynamic_string(dynamic_string_style='wait_animation', text_description=text_description, wait_style=wait_style, delay_time=delay_time, count=tmp_count)

            signal.signal(signal.SIGINT, test.signal_handler)
        
        subprocess_obj.terminate()
        subprocess_obj.wait()
        sys.exit(0)

if __name__ == '__main__':
    test = CommonFunc()
    test_subprocess = subprocess.Popen(args=f'python ../test_file.py', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    test.handle_signal(subprocess_obj=test_subprocess, text_description='事件模拟中')