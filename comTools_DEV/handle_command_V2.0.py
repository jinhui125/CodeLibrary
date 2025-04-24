# dateTime: 2025-04-23
# auther: jinhui

import os
import re
import sys
import time
import signal
import datetime
import subprocess

command_dict = {
					'获取命令帮助信息': '1', '执行Record录像功能': '2', '开启/关闭/重开远程': '3', '切换车端环境': '4', '模拟事故场景改造': '5',
				}

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