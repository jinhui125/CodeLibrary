import os
import re
import sys
import time
import signal
import datetime

class CommonFunc():

    def __init__(self):
        pass
    
    def progress_bar(t, description):
	
        for i in range(1, 101):
            print("\r{}: {}%: ".format(description, i), "▋" * (i // 2), end="", flush=True)
            time.sleep(t/100)

    def handle_signal(subprocess_obj, signal_flag, count = 1, text_description = "", wait_style = 'circle', delay_time = 0.25):
        wait_style_dict = {
                            'circle': ['\\', '|', '/', '-'], 
                            'columnar': ['▁', '▂', '▃', '▄', '▅', '▆', '▇', '█'],
                            'poker': ['♠️ ', '♥️ ', '♦️ ', '♣️ '],
                            'moon': ['🌕', '🌖', '🌗', '🌘', '🌑', '🌒', '🌓', '🌔'],
                            'clock': ['🕛', '🕐', '🕑', '🕒', '🕓', '🕔', '🕕', '🕖', '🕗', '🕘', '🕙', '🕚'],
                            # 'ellipsis': ['🂱', '🂲', '🂳', '🂴', '🂵', '🂶', '🂷', '🂸', '🂹', '🂺', '🂻', '🂼', '🂽', '🂾', '🂡', '🂢', '🂣', '🂤', '🂥', '🂦', '🂧', '🂨', '🂩', '🂪', 
                            # 			'🂫', '🂬', '🂭', '🂮', '🃁', '🃂', '🃃', '🃄', '🃅', '🃆', '🃇', '🃈', '🃉', '🃊', '🃋', '🃌', '🃍', '🃎', '🃑', '🃒', '🃓', '🃔', '🃕', '🃖', 
                            # 			'🃗', '🃘', '🃙', '🃚', '🃛', '🃜', '🃝', '🃞', '🃏']
                            }
        
        print(f'执行开始时间: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')

        while not signal_flag:
            try:
                count += 1
                print(f'\r{text_description}', f'{wait_style_dict[wait_style][count % len(wait_style_dict[wait_style])]}', end='', flush=True)
                time.sleep(delay_time)

            except KeyboardInterrupt:
                signal_flag = True
                os.killpg(os.getpgid(subprocess_obj.pid), signal.SIGKILL)
                subprocess_obj.wait()
                print('\n')
                sys.exit(0)
                break
                
            finally:
                pass

    def string_format(string, way, width, fill=' '):

        count = 0
        for word in string:
            if (word >= '\u4e00' and word <= '\u9fa5') or word in ['；', '：', '，', '（', '）', '！', '？', '——', '……',
                                                                '、', '》', '《']:
                count += 1
        width = width-count if width >= count else 0
        return '{0:{1}{2}{3}}'.format(string, fill, way, width)


    def table(col_ls: list, row_ls: list, l_width=50, r_width=3):

        title = [string_format(col_ls[0], '<', l_width, ' '),
                string_format(col_ls[1], '<', l_width, ' ')]
        content_ls = []
        for row in row_ls:
            content_ls.append([string_format(row[0], '<', l_width, ' '),
                            string_format(row[1], '>', r_width, ' ')])
        result = f"{'|'.join(title)}\n"
        for content in content_ls:
            result += f"{'|'.join(content)}\n"
        return result


    def replace_content(file, old_strs, new_strs, replace_mode = "replace", re_str = "", insert_index = ""):

        tmp_str = ''
        if bool(len(file)):
            with open(file=file, mode='r', encoding='utf-8') as fb:
                lines_ls = fb.readlines()
                for index in range(0, int(lines_ls.__len__())):
                    for i in range(0, int(old_strs.__len__())):
                        if old_strs[i] in lines_ls[index].strip():
                            print(lines_ls[index])
                            if replace_mode == "replace":
                                lines_ls[index] = f'{new_strs[i]}\n'
                            elif replace_mode == "modify":
                                lines_ls[index] = replace_content(file='', old_strs=lines_ls[index], new_strs=new_strs[i], replace_mode=replace_mode, re_str=re_str[i])
                            elif replace_mode == "append":
                                lines_ls[index] = replace_content(file='', old_strs=lines_ls[index], new_strs=new_strs[i], replace_mode=replace_mode, insert_index=insert_index)
                        else:
                            continue

                for i in range(0, int(lines_ls.__len__())):
                    tmp_str += lines_ls[i]

            with open(file=file, mode='w', encoding='utf-8') as fb:
                fb.write(tmp_str)
        else:
            tmp_list = []
            if replace_mode == 'modify':
                if re.search(pattern=re_str, string=old_strs):
                    index_tmp = re.search(pattern=re_str, string=old_strs).span()
                    tmp_list = [old_strs[0:index_tmp[0]], old_strs[index_tmp[0]:index_tmp[1]], old_strs[index_tmp[1]:]]
                    print(tmp_list)
                    tmp_list[1] = new_strs
                else:
                    tmp_list.append(old_strs)

            elif replace_mode == 'append':
                if insert_index != 1:
                    tmp_list = [old_strs[0:insert_index], old_strs[insert_index], old_strs[(insert_index+1):]]
                elif insert_index == len(old_strs):
                    tmp_list.append(old_strs + new_strs)
                else:
                    tmp_list.append(new_strs + old_strs)

            else:
                pass
            print(tmp_list)
            return "".join(tmp_list)
