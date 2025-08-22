#!/usr/bin/python
# -*- coding:utf-8 -*-
# @auther    : jinhui
# @dateTime  : 2025-08-19
# @function  : 公共方法类
# @version   : V1.0

import os
import re
import sys
import time
import signal
import datetime
import subprocess

class CommonFunc:

    def __init__(self, signal_flag = False):
        self.signal_flag = signal_flag
    
    def dynamic_string(self, dynamic_string_style, text_description, delay_time=0.25, bar_time=0, wait_style='circle', bar_style='▋', count=1):

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

    def handle_termination_signal(self, subprocess_obj, dynamic_string_style, text_description, wait_style='circle', bar_time=0, delay_time=0.25):

        print(f'开始执行时间: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
        tmp_count = 1

        while not self.signal_flag:

            if dynamic_string_style == 'proress_bar':
                self.dynamic_string(dynamic_string_style=dynamic_string_style, text_description=text_description, bar_time=bar_time)
                break

            elif dynamic_string_style == 'wait_animation':
                tmp_count += 1
                self.dynamic_string(dynamic_string_style=dynamic_string_style, text_description=text_description, wait_style=wait_style, delay_time=delay_time, count=tmp_count)
                signal.signal(signal.SIGINT, self.signal_handler)

            else:
                pass
        
        subprocess_obj.terminate() # windows系统终止信号用法
        # os.killpg(os.getpgid(subprocess_obj.pid), signal.SIGINT) # linux系统终止信号
        subprocess_obj.wait()
        sys.exit(0)

    def string_format(self, string, way, width, fill=' '):

        count = 0
        for word in string:
            if (word >= '\u4e00' and word <= '\u9fa5') or word in ['；', '：', '，', '（', '）', '！', '？', '——', '……',
                                                                '、', '》', '《']:
                count += 1
        width = width-count if width >= count else 0
        return f'{string:{fill}{way}{width}}'

    def table(self, data_ls: list, width_number=50, col_number = 2):

        split_row = '-' * width_number
        content_ls = []
        for i in range(len(data_ls)):
            if (i+1) % col_number != 0:
                content_ls.append([self.string_format(string=data_ls[i], way='^', width=width_number), self.string_format(string=data_ls[i+1], way='^', width=width_number)])
            else:
                continue
        print(f'-{split_row}-{split_row}-')
        for content in content_ls:
            print('|' + '|'.join(content) + '|')
            print(f'-{split_row}-{split_row}-')
    
    def contains_regex_in_file(self, file_path, pattern):
        with open(file_path, 'r', encoding='utf-8') as file:
            return re.search(pattern, file.read())

    def modify_content(self, file, match_str, replace_strs, mode='m', insert_index='', original_string=''):
        
        tmp_strs = ''
        if bool(os.path.exists(file)):
            with open(file=file, mode='r', encoding='utf-8') as fb:
                lines = fb.readlines()
                for line_index in range(len(lines)):
                    for index in range(len(match_str)):
                        if re.search(pattern=match_str[index], string=lines[line_index]):
                            if mode == 'm':
                                lines[line_index] = self.modify_content(file='', match_str=match_str[index], replace_strs=replace_strs[index], original_string=lines[line_index])
                            elif mode == 'a':
                                lines[line_index] = self.modify_content(file='', match_str=match_str[index], replace_strs=replace_strs[index], mode='a', original_string=lines[line_index], insert_index=insert_index)
                            else:
                                pass
                        else:
                            continue

                for i in range(len(lines)):
                    tmp_strs += lines[i]
            with open(file=file, mode='w', encoding='utf-8') as fb:
                fb.write(tmp_strs)
        else:
            tmp_ls = []
            tmp_str = ''
            if mode == 'm':
                if re.search(pattern=match_str, string=original_string):
                    index_tuple_ls = [match.span() for match in re.finditer(pattern=match_str, string=original_string)]
                    for i in range(len(index_tuple_ls)):
                        if i != 0:
                            tmp_str = ''.join(tmp_ls)
                            match_index = re.search(pattern=match_str, string=tmp_str).span()
                            tmp_ls = [tmp_str[0:int(match_index[0])], tmp_str[int(match_index[0]):int(match_index[1])], tmp_str[int(match_index[1]):]]
                            tmp_ls[1] = replace_strs
                        else:
                            tmp_ls = [original_string[0:int(index_tuple_ls[i][0])], original_string[int(index_tuple_ls[i][0]):int(index_tuple_ls[i][1])], original_string[int(index_tuple_ls[i][1]):]]
                            tmp_ls[1] = replace_strs
                else:
                    tmp_ls.append(original_string)
            elif mode == 'a':
                if insert_index != 1:
                    tmp_ls = [original_string[0:insert_index], replace_strs, original_string[insert_index:]]
                    print(tmp_ls)
                elif insert_index == len(original_string):
                    tmp_ls.append(original_string + replace_strs)
                else:
                    tmp_ls.append(replace_strs + original_string)
            else:
                pass
            return ''.join(tmp_ls)
        
    def handle_command(self, command, stdout=False):
        if not stdout:
            os.system(command=command)
        else:
            sp = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
            return sp.stdout.readlines()
        
if __name__ == '__main__':
    test = CommonFunc()
    # test_subprocess = subprocess.Popen(args=f'python ../test_file.py', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    # test.modify_content(file='./test.txt', match_str=[r'\bWuhan\b'], replace_strs=['Shanghai'], mode='a', insert_index=3)
    # test.modify_content(file='./config_deploy_6B.py', match_str=[r'domain = "idgops-(online|pre|opn|test)"', r'.format\((domain|"(idgops-(test|pre|opn|online))")\)'],
    #                                                 replace_strs=[r'domain = "idgops-test"', r'.format("idgops-test")'], mode='m')
    # test.table(data_ls=['车端环境名称', '车端环境字段', 'QA测试环境', 'pre', '线上运营环境', 'online', 'opn环境', 'opn', 'test环境', 'test'], width_number=30, col_number=2)
    # test.handle_termination_signal(subprocess_obj=test_subprocess, dynamic_string_style='proress_bar', text_description='正在录制Record中...', bar_time=10)
    test.modify_content(file='./patrol_checker_agent.conf', match_str=[r'fileexist_items { item_code: 1705003,', r'(1304126)[^( #事故)|^(,)]'],
                                                             replace_strs=[r'fileexist_items { item_code: 1304126,', r'1705003\n'])
    # mock_error_info = ['模拟事故场景', '模拟事故场景字段']
    # mock_error_info.extend(['自动驾驶异常—终点重启（1002）', '1', '传感器异常（1003）', '2', '自动驾驶严重异常-现场处置（1021）', '3', '传感器严重异常（1022）', '4', 'nvme严重异常（1023）', '5', 
    #                                 '轮胎异常（1004）', '6', '轮胎严重异常（1026）', '7', '交通事故', '8'])
    # test.table(data_ls=mock_error_info, width_number=35, col_number=2)
    # print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    
    # sp = subprocess.Popen(args=f'python3 {os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}/test_file.py', shell=True, stdout=subprocess.DEVNULL,
	# 							  stderr=subprocess.DEVNULL, start_new_session=True)
    # test.handle_termination_signal(subprocess_obj=sp, dynamic_string_style='wait_animation', text_description='事故场景模拟中')
 
